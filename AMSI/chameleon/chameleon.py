# This is a sample Python script.
import argparse
import base64
import ipaddress
import json
import os
import random
import re
import secrets
import string
import subprocess
import sys
import time
from datetime import datetime
from enum import Enum
from pathlib import Path

import numpy as np
from colorama import Fore


class AMSITrigger:
    def __init__(self):
        self.path = os.path.join(Utils.get_project_root(), "utils", "AMSITrigger.exe")
        self.args = "-f1"

    def check(self, filename):
        if not os.path.isfile(filename):
            Console.auto_line(f"[-] AMSITrigger: File {filename} not found")
            sys.exit(1)
        try:
            cmd = f"\"{self.path}\" {self.args} -i {filename}"
            # print(cmd)
            output = subprocess.check_output(cmd).decode().rstrip()
            if output.find("AMSI_RESULT_NOT_DETECTED") >= 0:
                Console.auto_line("  [+] SUCCESS: AMSI Bypassed!")
            elif output.find("Check Real Time protection is enabled") >= 0:
                Console.auto_line("  [#] UNKNOWN: Real-Time Protection Disabled")
            else:
                Console.auto_line("  [-] FAILED: AMSI Triggered!")
        except subprocess.CalledProcessError as e:
            for line in e.output.decode().split("\n"):
                if re.search(r"error", line):
                    print(f"  [-] Error: {line}")
                    sys.exit(1)


class Utils:

    @staticmethod
    def get_project_root():
        return str(Path(__file__).parent.absolute())


class PSContextType(Enum):
    MAIN = 0
    FUNCTION = 1
    NESTED_FUNCTION = 2
    PARAMS = 3
    COMMENTS = 4


class PSContext:
    def __init__(self, name: str, ctx_type: PSContextType):
        self.last_line = 0
        self.ctx_type = ctx_type
        self.name = name
        self.content = ""
        self.brackets = 0
        self.first_line = 0

    def open_brackets(self, nb=1):
        self.brackets += nb

    def close_brackets(self, nb=1):
        self.brackets -= nb

    def change_context(self, new_context):
        self.ctx_type = new_context


class PSTree:
    def __init__(self, psctx: PSContext):
        self.ctx = [psctx]

    @property
    def current(self) -> PSContext:
        if not self.is_empty():
            return self.ctx[-1]

    @property
    def current_ctx_type(self) -> PSContextType:
        if not self.is_empty():
            return self.ctx[-1].ctx_type

    @property
    def previous(self) -> PSContext:
        self.ctx.pop(-1)
        return self.current

    @property
    def balanced(self) -> bool:
        if not self.is_empty():
            return self.ctx[-1].brackets == 0

    def is_empty(self):
        return len(self.ctx) == 0

    def close(self):
        return self.ctx.pop(-1)

    def add_content(self, value):
        self.current.content += f"\n{value}"

    def open_brackets(self, nb=1):
        self.current.brackets += nb

    def close_brackets(self, nb=1):
        self.current.brackets -= nb

    def change_context(self, ctx_name: str, ctx_type: PSContextType):
        self.ctx.append(PSContext(ctx_name, ctx_type))

    def extract_data(self):
        var_pattern = re.compile(r'\$[\w|_]+')
        matches = [match.group() for match in var_pattern.finditer(self.current.content)]
        _matches = list(set(matches))
        matches = []
        for e in _matches:
            if e.lower() in ["$true", "$false", "$null", "$_"]:
                continue
            matches.append(e.strip().lower())
        matches.sort(key=len)
        return matches[::-1]

    def to_string(self):
        return "->".join([self.ctx[i].ctx_type.name for i in range(len(self.ctx))])


class ObfuscationLevel:
    def __init__(self, lvl_id=0):
        # Random string min and max size
        self.random_min = 25
        self.random_max = 1000
        # Junk size - Comments
        self.junk_min = 125
        self.junk_max = 2000
        # Function names
        self.function_min = 40
        self.function_max = 41
        # Token min and max size (min is 1)
        # Max=0: Unlimited
        self.token_min = 1
        self.token_max = 0
        # Case switcher iterations
        self.iterations = 6 if lvl_id == 0 else lvl_id

        if lvl_id == 1:
            self.random_min = 20
            self.random_max = 45

            self.junk_min = 25
            self.junk_max = 125

            self.function_min = 12
            self.function_max = 13

            self.token_min = 1
            self.token_max = 4
        elif lvl_id == 2:
            self.random_min = 75
            self.random_max = 125

            self.junk_min = 125
            self.junk_max = 250

            self.function_min = 40
            self.function_max = 41

            self.token_min = 1
            self.token_max = 3
        elif lvl_id == 3:
            self.random_min = 125
            self.random_max = 225

            self.junk_min = 125
            self.junk_max = 500

            self.function_min = 40
            self.function_max = 41

            self.token_min = 1
            self.token_max = 2

        elif lvl_id == 4:
            self.random_min = 225
            self.random_max = 325

            self.junk_min = 500
            self.junk_max = 1000

            self.function_min = 40
            self.function_max = 60

            self.token_min = 1
            self.token_max = 2

        elif lvl_id == 5:
            self.random_min = 500
            self.random_max = 750

            self.junk_min = 1000
            self.junk_max = 2000

            self.function_min = 50
            self.function_max = 60

            self.token_min = 1
            self.token_max = 1


class Chameleon:
    def __init__(self, filename, outfile, config: dict = None, lvl_id: int = 0, fmap: str = None, quiet: bool = False):
        self.content = None
        self.outfile = outfile
        self.eol = os.linesep
        self.load_from_file(filename=filename)
        self.quiet = quiet
        # Use case randomization
        self.case_randomization = config["cases"]

        self.level = ObfuscationLevel(lvl_id=lvl_id)
        # Use dictionary instead of random strings
        self.dictionary = None
        # This should be a mapping
        self.scoped_variables = []
        self.debug = False

        self.use_dictionary = config["random-type"] != "r"
        if self.use_dictionary:
            self.dictionary = open(os.path.join(Utils.get_project_root(), "dictionary", "food.txt"), "r").readlines()

        self.config = config
        self.function_mapping_file = fmap
        self.function_mapping = {}
        self.load_mapping(filename=fmap)

        self.placeholder = "####CHIMERA_COMMENT####"

        # Probabilities
        self.probabilities = {
            "backticker": 0.75,
            "case_randomize": 0.5
        }

        # Patterns
        self.nishang_patterns = open(
            os.path.join(
                Utils.get_project_root(),
                "config",
                "nishang.txt")
        ).readlines()

        # AMSI triggering strings
        self.default_patterns = open(
            os.path.join(
                Utils.get_project_root(),
                "config",
                "strings.txt")
        ).readlines()

        self.default_type_patterns = open(
            os.path.join(
                Utils.get_project_root(),
                "config",
                "data_types.txt")
        ).readlines()

        self.dont_backtick = [
            "kernel32",
            "ntdll"
        ]

    @staticmethod
    def scramble(text):
        new_text = ""
        for char in text:
            if char.islower():
                new_text += secrets.choice(string.ascii_lowercase)
            else:
                new_text += char
        return new_text

    def load_from_file(self, filename):
        if not os.path.isfile(filename):
            Console.auto_line("[-] File not found")
            sys.exit(1)
        with open(filename, 'r') as in_file:
            self.content = in_file.read()
        if not len(self.content.split(self.eol)) > 1:
            self.eol = "\n"

    def load_mapping(self, filename):
        if not filename:
            return
        if filename and not os.path.isfile(filename):
            Console.auto_line("[-] Mapping file not found")
        try:
            with open(filename, 'r') as in_file:
                self.function_mapping = json.load(in_file)
        except:
            Console.warn_line("  [-] Wrong mapping format. Skipping")

    def save_mapping(self):
        try:
            with open(self.function_mapping_file, 'w') as out_file:
                json.dump(self.function_mapping, out_file)
        except:
            Console.auto_line("  [-] Error saving mapping")

    def random_ascii_string(self, min_size=None, max_size=None):
        if not min_size:
            min_size = self.level.random_min
        if not max_size:
            max_size = self.level.random_max
        if self.config["random-type"] == "d":
            return self.create_random_word(min_size=min_size, max_size=max_size)
        return ''.join(secrets.choice(string.ascii_letters) for _ in range(random.randint(min_size, max_size)))

    def random_alpha_string(self, min_size=None, max_size=None):
        if not min_size:
            min_size = self.level.random_min
        if not max_size:
            max_size = self.level.random_max
        if self.config["random-type"] == "d":
            return self.create_random_word(min_size=min_size, max_size=max_size)
        return ''.join(
            secrets.choice(string.ascii_letters + string.digits) for _ in range(random.randint(min_size, max_size)))

    def random_variable(self, min_size=None, max_size=None):
        return f"${self.random_alpha_string(min_size=min_size, max_size=max_size)}"

    def tokenize(self, input_string, min_size=None, max_size=None):
        if not min_size:
            min_size = self.level.token_min
        if not max_size:
            max_size = self.level.token_max
        ret = []
        i = 0
        while i < len(input_string):
            j = max(random.SystemRandom().randint(i, i + max_size if max_size else len(input_string)), min_size)
            if i != j:
                ret.append(input_string[i:j])
                i = j
        return ret

    def randomize_cases(self):
        var_pattern = re.compile(r'\$[\w|_]+', re.IGNORECASE)
        data_type_pattern1 = re.compile(r"(?<=New-Object ).+?(?=[\(\-\@])", re.IGNORECASE)
        data_type_pattern2 = re.compile(r"(?<=\[)([\w]+\.)+[\w]+?(?=\])", re.IGNORECASE)
        matches = [match.group().strip() for match in var_pattern.finditer(self.content)]
        dt_new_obj_matches = [match.group().strip() for match in data_type_pattern1.finditer(self.content)]
        dt_brackets_matches = [match.group().strip() for match in data_type_pattern2.finditer(self.content)]

        for match in dt_new_obj_matches:
            extract = None
            if match.lower().find("typename") > -1:
                regex = r"(?<=-TypeName).+?(?=\s)"
                pattern = re.compile(regex, re.IGNORECASE)
                raw = pattern.search(match + " ")
                if raw:
                    extract = raw.group().strip()
                else:
                    if self.debug:
                        Console.fail_line(match)
            else:
                extract = match
            if extract:
                dt_brackets_matches.append(extract)

            # Console.warn_line(extract)

        matches += dt_brackets_matches
        matches = list(set(matches))
        matches.sort(key=len)
        matches = matches[::-1]
        for match in matches:
            self.content = self.content.replace(
                match,
                self.case_randomize(match)
            )

    def case_randomize(self, input_string: str, probability: float = None):
        if not probability:
            probability = self.probabilities["case_randomize"]
        ret = ""
        for s in input_string:
            if np.random.binomial(1, probability):
                ret += s.upper()
            else:
                ret += s.lower()
        return ret

    def convert_decimal(self):

        wrapper = ["iex", "exit"]
        w = []
        if self.config["backticks"]:
            for wrap in wrapper:
                w.append(self.backticker(wrap))
        else:
            w = wrapper
        self.content = f"{w[0]}(-join(({','.join([str(int(b)) for b in self.content.encode()])})|%{{[char]$_}}));{w[1]}"

    def convert_base64(self):
        wrapper = ["iex", "exit"]
        w = []

        enc = "[System.Text.Encoding]::UTF8.GetString"
        conv = "[System.Convert]::FromBase64String"
        if self.config["cases"]:
            enc = self.case_randomize(enc)
            conv = self.case_randomize(conv)
        payload = base64.b64encode(self.content.encode()).decode()
        if self.config["backticks"]:
            for wrap in wrapper:
                w.append(self.backticker(wrap))
            payload = self.backticker(payload)
        else:
            w = wrapper

        self.content = f"{w[0]}(" \
                       f"{enc}(" \
                       f"{conv}('{payload}')));{w[1]}"

    def replace_comments(self):
        # Get rid of <# ... #> comments
        text = self.content
        rows = []
        _content = text.encode().decode(encoding="windows-1252", errors="replace")
        start = False
        matches = re.finditer(r"<#[^#]+#>", _content, re.MULTILINE)
        for _, match in enumerate(matches, start=1):
            _content = _content.replace(match.group(), self.placeholder)
        text = _content.split(self.eol)

        for nr, row in enumerate(text, start=1):
            if row.find("<#") > -1:
                start = True
            if row.find("#>") > -1:
                start = False
            if not start:
                rows.append(row)
        _content = self.eol.join(rows)

        # Single Line Comments
        slc_pattern = re.compile(r"#.+")
        s1_pattern = re.compile(r"\"([^\"]*)\"")
        s2_pattern = re.compile(r"'([^']*)'")
        for line in rows:
            match = slc_pattern.search(line)
            if match:
                # Single string, we don't do anything = won't break the script
                res = [s1_pattern.search(line), s2_pattern.search(line)]
                if any(res):
                    res = [r.group() for r in res if r and r.group().find("#") > -1]
                else:
                    res = []
                if len(res) > 0:
                    continue

                _content = _content.replace(match.group(), self.placeholder)
                self.content = _content

    def remove_comment_placeholders(self):
        while self.content.find(self.placeholder) >= 0:
            # Replace each occurrence with a new random string
            self.content = self.content.replace(self.placeholder, "")

    def insert_comments(self):
        while self.content.find(self.placeholder) >= 0:
            # Replace each occurrence with a new random string
            self.content = self.content.replace(self.placeholder, self.create_junk(prefix="#"), 1)

    def random_backtick(self):
        # Pattern 1 and 2 are still unsafe to use
        string_pattern1 = re.compile(r'"([^\"]+)"')
        string_pattern2 = re.compile(r"'([^\']+)'")
        function_pattern = re.compile(r'function\s+([\w\-\:]+)')
        _content = self.content.split(self.eol)
        for n, line in enumerate(_content, start=0):
            f = function_pattern.search(line)
            s1 = string_pattern1.search(line)
            s2 = string_pattern2.search(line)
            _t = 0
            if f:
                _t = 1
                repl = [p.groups()[0] for p in function_pattern.finditer(line)]
            elif s1 and False:
                repl = [p.groups()[0] for p in string_pattern1.finditer(line)]
            elif s2:
                repl = [p.groups()[0] for p in string_pattern2.finditer(line)]
            else:
                continue
            for match in repl:
                if _t == 1 and match.find(":") > -1:
                    match = match.split(":")[1]
                if _t == 1 and match.find("(") > -1:
                    match = match.split("(")[0]

                if match in self.dont_backtick:
                    continue
                if _t < 1 or match.find("$") + line.find("[") + line.find("]") > -3 or line.count(
                        match) > 1 or re.search(r"[\w]+", match) is None:
                    continue
                _content[n] = line.replace(match, self.backticker(match))

        self.content = self.eol.join(_content)

    def backticker(self, input_string: str, probability: float = None):
        if not probability:
            probability = self.probabilities["backticker"]
        ret = ""
        for char in input_string:
            backtick = '`'
            # % chance an input character will be backticked (default 75%)
            if np.random.binomial(1, probability):
                backtick = ''
            if char in "a0befnrtuxv":
                backtick = ''
            ret += f"{backtick}{char}"
        return ret

    def custom_backticker(self, strings: list):
        for s in strings:
            rs = s
            # If case randomization is enabled, perform it before the backtick is applied
            if self.case_randomization:
                rs = self.case_randomize(s)
            self.content = self.content.replace(s, self.backticker(rs))

    def nishang_script(self):
        for pattern in self.nishang_patterns:
            pattern = re.compile(pattern, re.IGNORECASE)
            self.content = pattern.sub("", self.content)

    def indentation_randomization(self):
        lines = self.content.split(self.eol)
        space_pattern = re.compile(r"^\s+")
        for n, line in enumerate(lines, start=0):
            new_line = space_pattern.sub(" " * np.random.randint(0, 10), line)
            lines[n] = new_line
        self.content = self.eol.join(lines)

    def safety_check(self, target):
        clean = True
        matches = []
        for regex in [rf"[\w\.]{target}", rf"{target}[\w\.]"]:
            pattern = re.compile(regex, re.IGNORECASE)
            matches = [match.group().strip() for match in pattern.finditer(self.content)]
        if len(matches) > 0:
            clean = False
        return clean

    def transformer(self, target_patterns=None, regex=None, strict=True):
        if self.debug:
            print()
        if not target_patterns:
            target_patterns = self.default_patterns
        mapping = {}
        pattern = re.compile(regex, re.IGNORECASE)
        matches = [match.group().strip() for match in pattern.finditer(self.content)]
        matches = list(set(matches))

        for match in matches:
            red_flag = ""
            if strict and match.lower() not in target_patterns:
                if self.debug:
                    Console.warn_line(f"[D] {match} is not a red flag")
                continue
            elif not strict:
                for rf in target_patterns:
                    if not re.search(rf"[\s]+{rf}", match, re.IGNORECASE):
                        continue
                    if self.debug:
                        Console.warn_line(f"[+] {rf} found in {match}")
                    red_flag = rf
                    break
            else:
                red_flag = match
            if red_flag == "":
                if self.debug:
                    Console.warn_line(f"[D] {match} is not a red flag")
                continue
            if not self.safety_check(red_flag):
                continue
            if self.debug:
                Console.warn_line(f"[+] Red flag {red_flag} found")
            green_flag = self.random_variable()
            tokens = self.tokenize(red_flag)
            for token in tokens:
                if self.config["backticks"]:
                    token = self.backticker(token)
                mapping[self.random_variable()] = f'"{token}"'

            mapping[green_flag] = f"({' + '.join(mapping.keys())})"

            self.content = self.content.replace(red_flag, green_flag)
        raw = self.eol.join([f"{k} = {v}{self.eol}" for k, v in mapping.items()])
        self.content = raw + self.content

    def replace_strings(self, targets_strings=None):
        if not targets_strings:
            targets_strings = self.default_patterns
        regex = r"(?<=').+?(?=')"
        self.transformer(target_patterns=targets_strings, regex=regex, strict=False)
        regex = r'(?<=").+?(?=")'
        self.transformer(target_patterns=targets_strings, regex=regex, strict=False)
        regex = r'(?<=\.)[\w]+?(?=\()'
        self.transformer(target_patterns=targets_strings, regex=regex, strict=True)

    def replace_functions(self):
        function_pattern = re.compile(r'function\s+([\w|\_|\-]+)')
        matches = [match.groups()[0] for match in function_pattern.finditer(self.content)]
        matches.sort(key=len)
        matches = matches[::-1]
        for match in matches:
            if match in self.function_mapping.keys():
                repl = self.function_mapping[match]['repl']
            else:
                continue
            if match in "".join(["function", "filter"]):
                if self.function_mapping:
                    self.function_mapping.pop(match)
                continue
            if not self.safety_check(match):
                if self.function_mapping:
                    self.function_mapping.pop(match)
                continue

            self.content = self.content.replace(
                match,
                repl
            )

    def replace_variables(self):
        special_vars = {
            "$null": self.random_variable(),
            "$true": self.random_variable(),
            "$false": self.random_variable(),
            "$args": self.random_variable(),
            "$_": self.random_variable()
        }

        if self.config["tfn-values"]:
            # Without AST parsing, it's kinda difficult to fix variable scoping issues
            # with TFN, the values $true, $false and $null are replaced at global and "maybe"
            # in-function scope

            # Issue 1: $true, $false and $null should be declared with global scope
            for k, v in special_vars.items():
                # Self is untouchable
                if k == "$_":
                    continue
                # Args is untouchable
                if k == "$args":
                    continue
                self.content = self.content.replace(k, v)
                self.content = f"{v} = {k}\n{self.content}"

            # Issue 2: $true, $false and $null should be declared at function scope
            function_pattern = re.compile(r'function\s+[\w|\_|\-]+\s*\{', re.MULTILINE)
            for match in function_pattern.finditer(self.content):
                self.content = self.content.replace(
                    match.group(),
                    match.group() + "\n" + "\n".join([f"{v} = {k}" for k, v in special_vars.items()])
                )

        var_pattern = re.compile(r'\$[\w|_]+')
        matches = [match.group() for match in var_pattern.finditer(self.content)]
        matches = list(set(matches))
        matches.sort(key=len)
        matches = matches[::-1]
        for match in matches:
            # if not self.safety_check(matches):
            #    continue
            if match.strip().lower() in self.scoped_variables or match.strip().lower() in "".join(
                    self.scoped_variables):
                continue
            elif match.strip().lower() in special_vars.keys() or re.search(r"^\$env", match, re.IGNORECASE):
                continue
            else:
                self.content = self.content.replace(match, self.random_variable())

    def replace_data_types(self, target_data_types=None):
        if not target_data_types:
            target_data_types = self.default_type_patterns
        # regex = r"(?<=\[).+?(?=\])"
        # self.transformer(target_patterns=target_data_types, regex=regex)
        regex = r"(?<=New-Object )[^\-]+?(?=[\(\-\@\)])"
        self.transformer(target_patterns=target_data_types, regex=regex)
        regex = r"(?<=-TypeName).+?(?=\s)"
        self.transformer(target_patterns=target_data_types, regex=regex)

    def create_word(self):
        ret = ""
        if self.config["random-type"] != "r":
            ret += str(secrets.choice(self.dictionary)).strip(" " + self.eol).capitalize()
        else:
            ret = self.random_ascii_string(3, 15)
        return ret

    def create_random_word(self, min_size=None, max_size=None):
        ret = ""
        size = np.random.randint(min_size, max_size)
        while len(ret) < size:
            ret += str(secrets.choice(self.dictionary)).capitalize().strip()
        return ret

    def create_junk(self, prefix="#"):
        junk_text = f"{prefix}"
        junk_size = np.random.randint(self.level.junk_min, self.level.junk_max)
        current_line_length = 0
        while len(junk_text) <= junk_size:
            next_word = " " + self.create_word()
            if current_line_length <= 80:
                junk_text += next_word
                current_line_length += len(next_word)
            else:
                junk_text += f"{self.eol}{prefix}{' ' * np.random.randint(0, 5)}{next_word}"
                current_line_length = 0
        return junk_text

    def hex_address(self):
        ip_regex = r"(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
        ip_pattern = re.compile(ip_regex)
        matches = ip_pattern.finditer(self.content)
        for _, match in enumerate(matches, start=1):
            # convert `192.168.56.101` to `0xC0A83865`
            hexified = hex(int(ipaddress.IPv4Address(match.group())))
            self.content = self.content.replace(match.group(), hexified)

    def identify_reflective_constructors(self):
        content = self.content.split(self.eol)
        var_pattern = re.compile(r'\$[\w|_]+')
        all_vars = []
        for n, line in enumerate(content, start=0):
            if line.lower().find("customattribute") > -1:
                ob = line[line.lower().find("customattribute"):].count("(")
                offset = 1
                search_area = line
                while ob != 0 or offset >= len(content):
                    search_area += f" {content[n + offset]}"
                    offset += 1
                    ob = search_area.count("(") - search_area.count(")")
                _vars = [var.group().strip().lower() for var in var_pattern.finditer(search_area)]
                all_vars += _vars
        all_vars = list(set(all_vars))
        if self.debug:
            print(f"[+] Adding {all_vars}")
        self.scoped_variables += all_vars

    def identify_scoped_variables(self):
        tree = PSTree(
            psctx=PSContext(name="main", ctx_type=PSContextType.MAIN)
        )

        mapping = {}
        function = ""
        content = self.content.split(self.eol)
        for n, line in enumerate(content, start=1):
            state_changed = False
            see_next = False
            tree.current.current_line = n
            function_match = None
            param_match = None
            ob = 0
            cb = 0
            tree.add_content(line)
            if tree.current_ctx_type in [PSContextType.MAIN, PSContextType.FUNCTION, PSContextType.NESTED_FUNCTION]:
                function_match = re.search(r"(filter|function)\s+([\w][^\s]+)[\{\s]?", line, re.IGNORECASE)
                param_match = re.search(r"param[\s|\n|\r|\(]*\(?", line, re.IGNORECASE)

                if function_match:
                    function = function_match.groups()[1].split("(")[0]
                    if function.find(":") > -1:
                        function = function.split(":")[1]
                    if tree.current_ctx_type == PSContextType.MAIN:
                        if self.debug:
                            print(f"Found new function {function} at line: {n}")
                        tree.change_context(ctx_name=function, ctx_type=PSContextType.FUNCTION)
                        see_next = True
                    elif tree.current_ctx_type == PSContextType.FUNCTION:
                        if self.debug:
                            print(f"Found new nested function {function} at line: {n}")
                        tree.change_context(ctx_name=function, ctx_type=PSContextType.NESTED_FUNCTION)
                        see_next = True
                    ob = line.count("{")
                    if ob == 0:
                        see_next = True
                    else:
                        if self.debug:
                            print(f"Function starts at line: {n}")
                    cb = line.count("}")
                elif param_match:
                    tree.change_context(ctx_name=tree.current.name + "-param", ctx_type=PSContextType.PARAMS)
                    ob = line.count("(")
                    cb = line.count(")")
                    if ob == 0:
                        see_next = True
                    else:
                        if self.debug:
                            print(f"Param() start at line: {n}")
                else:
                    ob = line.count("{")
                    cb = line.count("}")
            elif tree.current_ctx_type == PSContextType.PARAMS:
                ob = line.count("(")
                cb = line.count(")")
                if ob == 0 and cb == 0:
                    see_next = True
            else:
                continue
            tree.open_brackets(nb=ob)
            tree.close_brackets(nb=cb)

            if tree.balanced and not see_next:
                if tree.current_ctx_type == PSContextType.PARAMS:
                    params = tree.extract_data()
                    if self.debug:
                        print(f"  > Found parameters: {params}")
                    mapping[function] = params
                    self.scoped_variables += params
                    # Close parameters context
                    if self.debug:
                        print(f"Param() close at line {n}")
                    tree.close()
                elif tree.current_ctx_type == PSContextType.NESTED_FUNCTION:
                    # Close function context
                    if self.debug:
                        print(f"Nested function closes at line {n}")
                    tree.close()
                elif tree.current_ctx_type == PSContextType.FUNCTION:
                    # Close function context
                    if self.debug:
                        print(f"Function closes at line {n}")
                    tree.close()
        if not self.function_mapping:
            Console.auto("    [>] Generating function mapping... ", quiet=self.quiet)
            self.generate_mapping(mapping)
            self.save_mapping()
            Console.auto_line("Success", quiet=self.quiet)
        self.clean_scoped_variables()

    def generate_mapping(self, mapping, scope="function"):
        new_mapping = {}
        for k, v in mapping.items():
            new_params = {}
            new_params["original"] = v
            new_params["repl"] = [Chameleon.scramble(param) if scope != "function" else param for param in v]

            new_mapping[k] = {
                "repl": self.random_ascii_string(
                    min_size=self.level.function_min,
                    max_size=self.level.function_max
                ) if scope else k,
                "params": new_params
            }
        # Updating the global mapping
        self.function_mapping = new_mapping
        # Forcing a default file name
        self.function_mapping_file = "function_mapping.json"

    def clean_scoped_variables(self):
        self.scoped_variables = list(set(self.scoped_variables))

    def obfuscate(self):

        Console.auto("  [*] Zeroing out comments... ", quiet=self.quiet)
        self.replace_comments()
        Console.auto_line("Done", quiet=self.quiet)

        Console.auto_line("[+] Chameleon: standard obfuscation", quiet=self.quiet)

        Console.auto_line("  [*] Identifying scoped variables and reflective constructors", quiet=self.quiet)
        if self.config["safe"]:
            self.identify_reflective_constructors()
        self.identify_scoped_variables()
        if len(self.scoped_variables) > 0:
            if self.config["verbose"]:
                Console.auto_line("    [>] These variables will not be obfuscated", quiet=self.quiet)
                Console.auto_line(f"    [>] {', '.join(self.scoped_variables)}", quiet=self.quiet)
            else:
                Console.auto_line(f"    [>] Identified {len(self.scoped_variables)} scoped variables "
                                  f"which will not be obfuscated", quiet=self.quiet)
        else:
            Console.auto_line("    [-] No variables found", quiet=self.quiet)
        if self.config["variables"]:
            Console.auto("  [*] Variables Obfuscation... ", quiet=self.quiet)
            self.replace_variables()
            Console.auto_line("Done", quiet=self.quiet)
        if self.config["data-types"]:
            Console.auto("  [*] Data Types Obfuscation... ", quiet=self.quiet)
            self.replace_data_types()
            Console.auto_line("Done", quiet=self.quiet)
        if self.config["functions"]:
            Console.auto("  [*] Function Obfuscation... ", quiet=self.quiet)
            self.replace_functions()
            Console.auto_line("Done", quiet=self.quiet)
        if self.config["nishang"]:
            Console.auto("  [*] Nishang Obfuscation... ", quiet=self.quiet)
            self.nishang_script()
            Console.auto_line("Done", quiet=self.quiet)
        if self.config["cases"]:
            Console.auto("  [*] Cases randomization... ", quiet=self.quiet)
            self.randomize_cases()
            Console.auto_line("Done", quiet=self.quiet)
        if self.config["hex-ip"]:
            Console.auto("  [*] IP Address to Hex... ", quiet=self.quiet)
            self.hex_address()
            Console.auto_line("Done", quiet=self.quiet)
        if self.config["comments"]:
            Console.auto("  [*] Comments Obfuscation... ", quiet=self.quiet)
            self.insert_comments()
            Console.auto_line("Done", quiet=self.quiet)
        else:
            Console.auto("  [*] Removing comment placeholders... ", quiet=self.quiet)
            self.remove_comment_placeholders()
            Console.auto_line("Done", quiet=self.quiet)
        if self.config["spaces"]:
            Console.auto("  [*] Indentation Randomization... ", quiet=self.quiet)
            self.indentation_randomization()
            Console.auto_line("Done", quiet=self.quiet)
        if self.config["strings"]:
            Console.auto("  [*] Strings Obfuscation... ", quiet=self.quiet)
            self.replace_strings()
            Console.auto_line("Done", quiet=self.quiet)
        if self.config["random-backticks"]:
            Console.auto("  [*] Random Backticking... ", quiet=self.quiet)
            self.random_backtick()
            Console.auto_line("Done", quiet=self.quiet)
        Console.auto_line("[+] Chameleon: obfuscation via encoding", quiet=self.quiet)
        if self.config["decimal"]:
            Console.auto("  [*] Converting to decimal... ", quiet=self.quiet)
            self.convert_decimal()
            Console.auto_line("Done", quiet=self.quiet)
        if self.config["base64"]:
            Console.auto("  [*] Converting to base64... ", quiet=self.quiet)
            self.convert_base64()
            Console.auto_line("Done", quiet=self.quiet)

    def write_file(self):
        Console.auto(f"  [*] Writing obfuscated payload to {self.outfile}... ", quiet=self.quiet)
        with open(self.outfile, "w") as out:
            out.write(self.content)
            Console.auto_line("Done", quiet=self.quiet)
        # print(self.content)


class Console:

    @staticmethod
    def write(what, color=Fore.WHITE):
        index = what.find("]")
        if index > -1:
            what = f"{color}{what[:index + 1]}{Fore.WHITE}{what[index + 1:]}"
        else:
            what = f"{color}{what}{Fore.WHITE}"
        print(what, end='')

    @staticmethod
    def write_line(what, color=Fore.WHITE):
        index = what.find("]")
        if index > -1:
            what = f"{color}{what[:index + 1]}{Fore.WHITE}{what[index + 1:]}{Fore.WHITE}"
        else:
            what = f"{color}{what}{Fore.WHITE}"
        print(what)

    @staticmethod
    def success(what):
        Console.write(what=what, color=Fore.GREEN)

    @staticmethod
    def success_line(what):
        Console.write_line(what=what, color=Fore.GREEN)

    @staticmethod
    def fail(what):
        Console.write(what=what, color=Fore.RED)

    @staticmethod
    def fail_line(what):
        Console.write_line(what=what, color=Fore.RED)

    @staticmethod
    def info(what):
        Console.write(what=what, color=Fore.BLUE)

    @staticmethod
    def info_line(what):
        Console.write_line(what=what, color=Fore.BLUE)

    @staticmethod
    def progress(what):
        Console.write(what=what, color=Fore.CYAN)

    @staticmethod
    def progress_line(what):
        Console.write_line(what=what, color=Fore.CYAN)

    @staticmethod
    def warn(what):
        Console.write(what=what, color=Fore.YELLOW)

    @staticmethod
    def warn_line(what):
        Console.write_line(what=what, color=Fore.YELLOW)

    @staticmethod
    def auto(what, quiet=False):
        if quiet:
            return
        if what.find("[+]") > -1:
            Console.success(what=what)
        elif what.find("[*]") > -1:
            Console.info(what=what)
        elif what.find("[>]") > -1:
            Console.progress(what=what)
        elif what.find("[#]") > -1:
            Console.warn(what=what)
        elif what.find("[-]") > -1:
            Console.fail(what=what)
        elif what == "Success" or what == "Done":
            Console.success(what=what)
        elif what == "Fail":
            Console.fail(what=what)
        else:
            Console.write(what=what)

    @staticmethod
    def auto_line(what, quiet=False):
        if quiet:
            return
        if what.find("[+]") > -1:
            Console.success_line(what=what)
        elif what.find("[*]") > -1:
            Console.info_line(what=what)
        elif what.find("[>]") > -1:
            Console.progress_line(what=what)
        elif what.find("[#]") > -1:
            Console.warn_line(what=what)
        elif what.find("[-]") > -1:
            Console.fail_line(what=what)
        elif what == "Success" or what == "Done":
            Console.write_line(what=what, color=Fore.LIGHTWHITE_EX)
        elif what == "Fail":
            Console.fail_line(what=what)
        else:
            Console.write_line(what=what)


def welcome():
    banner = rf"""{Fore.RED}__________________________________________________________________________________
    
  {Fore.LIGHTRED_EX}▒▒▒▒▒▒  {Fore.RED}▒▒   ▒▒ {Fore.LIGHTBLUE_EX} ▒▒▒▒▒  {Fore.BLUE}▒▒▒    ▒▒▒ {Fore.LIGHTYELLOW_EX}▒▒▒▒▒▒▒ {Fore.YELLOW}▒▒     {Fore.LIGHTGREEN_EX}▒▒▒▒▒▒▒ {Fore.GREEN} ▒▒▒▒▒  {Fore.LIGHTCYAN_EX}▒▒▒  ▒▒ {Fore.CYAN} ▒▒▒
  {Fore.LIGHTRED_EX}▒▒      {Fore.RED}▒▒   ▒▒ {Fore.LIGHTBLUE_EX}▒▒   ▒▒ {Fore.BLUE}▒▒▒▒  ▒▒▒▒ {Fore.LIGHTYELLOW_EX}▒▒      {Fore.YELLOW}▒▒     {Fore.LIGHTGREEN_EX}▒▒      {Fore.GREEN}▒▒   ▒▒ {Fore.LIGHTCYAN_EX}▒▒▒▒ ▒▒ {Fore.CYAN}▒▒▒▒
  {Fore.LIGHTRED_EX}▓▓      {Fore.RED}▓▓▓▓▓▓▓ {Fore.LIGHTBLUE_EX}▓▓▓▓▓▓▓ {Fore.BLUE}▓▓ ▓▓▓▓ ▓▓ {Fore.LIGHTYELLOW_EX}▓▓▓▓▓   {Fore.YELLOW}▓▓     {Fore.LIGHTGREEN_EX}▓▓▓▓▓   {Fore.GREEN}▓▓   ▓▓ {Fore.LIGHTCYAN_EX}▓▓ ▓▓▓▓ {Fore.CYAN}  ▓▓
  {Fore.LIGHTRED_EX}██      {Fore.RED}██   ██ {Fore.LIGHTBLUE_EX}██   ██ {Fore.BLUE}██  ██  ██ {Fore.LIGHTYELLOW_EX}██      {Fore.YELLOW}██     {Fore.LIGHTGREEN_EX}██      {Fore.GREEN}██   ██ {Fore.LIGHTCYAN_EX}██  ███ {Fore.CYAN}  ██
  {Fore.LIGHTRED_EX}██████  {Fore.RED}██   ██ {Fore.LIGHTBLUE_EX}██   ██ {Fore.BLUE}██      ██ {Fore.LIGHTYELLOW_EX}███████ {Fore.YELLOW}██████ {Fore.LIGHTGREEN_EX}███████ {Fore.GREEN} █████  {Fore.LIGHTCYAN_EX}██   ██ {Fore.CYAN}  ██
{Fore.RED}----------------------------------------------------------------------------------{Fore.LIGHTWHITE_EX}
▒ by d3adc0de (@klezVirus)
{Fore.RED}__________________________________________________________________________________{Fore.WHITE}

"""
    # mind-blowing banner rendering
    os.system('color')

    for n, line in enumerate(banner.split("\n"), start=0):
        for char in line:
            print(char, end='', flush=True)
            # time.sleep(0.0001)
        if n < len(banner.split("\n")) - 1:
            print()
        time.sleep(0.1)


def author():
    info = {
        "whoami": "d3adc0de (@klezVirus)",
        "groups d3adc0de": "d3adc0de : authors",
        "echo $HOME": "https://github.com/klezVirus",
        "credits": "@tokyoneon_"
    }
    # mind-blowing banner rendering
    os.system('color')
    print(Fore.LIGHTBLACK_EX + "▩" * 82)

    for cmd, out in info.items():
        print(f"{Fore.WHITE}▒ {Fore.LIGHTGREEN_EX}$ ", end='', flush=True)
        time.sleep(0.5)
        for char in cmd:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print()
        print(f"{Fore.WHITE}▒ ", end='', flush=True)
        time.sleep(0.5)
        print(f"{Fore.LIGHTCYAN_EX}{out}{Fore.WHITE}")
        time.sleep(0.3)
    print(Fore.LIGHTBLACK_EX + "▩" * 82 + Fore.WHITE)
    time.sleep(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Chameleon - PowerShell script obfuscator (Improved Python port of Chimera)'
    )

    parser.add_argument(
        '-l', '--level', required=False, type=int, choices=list(range(6)), default=0,
        help='String manipulation Level (1: MIN, 5: MAX, 0: RANDOM)')
    parser.add_argument(
        '-o', '--output', required=True, type=str, default=None, help='Store the payload in a file')
    parser.add_argument(
        '-v', '--variables', required=False, action="store_true", help='Enable variable obfuscation')
    parser.add_argument(
        '-s', '--strings', required=False, action="store_true", help='Enable string obfuscation')
    parser.add_argument(
        '-d', '--data-types', required=False, action="store_true", help='Enable data types obfuscation')
    parser.add_argument(
        '-n', '--nishang', required=False, action="store_true", help='Enable Nishang scripts obfuscation')
    parser.add_argument(
        '-c', '--comments', required=False, action="store_true", help='Enable comments obfuscation')
    parser.add_argument(
        '-f', '--functions', required=False, action="store_true", help='Enable functions obfuscation')
    parser.add_argument(
        '-b', '--use-backticks', required=False, action="store_true",
        help='Enable use of backticks with generated strings')
    parser.add_argument(
        '--random-backticks', required=False, action="store_true", help='Enable use of backticks randomization')
    parser.add_argument(
        '-r', '--random-cases', required=False, action="store_true", help='Enable upper/lower randomization')
    parser.add_argument(
        '-i', '--random-spaces', required=False, action="store_true", help='Enable indentation randomization')
    parser.add_argument(
        '-x', '--hex-ip', required=False, action="store_true", help='Enable indentation randomization')
    parser.add_argument(
        '-j', '--true-false-null', required=False, action="store_true",
        help='Try and obfuscate $true, $false and $null (experimental)')
    parser.add_argument(
        '-a', '--enable-all', required=False, action="store_true", help='Enable all obfuscation types')
    parser.add_argument(
        '--decimal', required=False, action="store_true", help='Convert obfuscated payload to decimal format')
    parser.add_argument(
        '--base64', required=False, action="store_true", help='Convert obfuscated payload to base64 format')
    parser.add_argument(
        '-z', '--check', required=False, action="store_true",
        help='Check the script against AMSI Trigger (@RythmStick, @rasta-mouse)')
    parser.add_argument(
        '-F', '--function-mapping', required=False, type=str, help='Add custom keywords to obfuscate')
    parser.add_argument(
        '-K', '--keywords', required=False, action="append", help='Add custom keywords to obfuscate')
    parser.add_argument(
        '-B', '--backticks', required=False, action="append", help='Add a list of words to backtick')
    parser.add_argument(
        '-t', '--randomization-type', required=False, type=str, choices=['r', 'd', 'h'], default='r',
        help='Type of randomization (r: Random, d: Dictionary, h: Hybrid)')
    parser.add_argument(
        '--safe', required=False, action="store_true", help='Reduce obfuscation of certain variables')
    parser.add_argument(
        '--verbose', required=False, action="store_true", help='Enable verbose output')
    parser.add_argument(
        '--about', required=False, action="store_true", help='Shows additional information about the tool')
    parser.add_argument(
        'target', default=None, help='Script to obfuscate')

    try:
        sys.argv.index("--about")
        welcome()
        author()
        if len(sys.argv) == 2:
            sys.exit(0)
    except ValueError:
        pass

    args = parser.parse_args()

    welcome()
    level = args.level
    config = {
        "strings": args.strings or args.enable_all,
        "variables": args.variables or args.enable_all,
        "data-types": args.data_types or args.enable_all,
        "functions": args.functions or args.enable_all,
        "comments": args.comments or args.enable_all,
        "spaces": args.random_spaces or args.enable_all,
        "cases": args.random_cases or args.enable_all,
        "nishang": args.nishang or args.enable_all,
        "backticks": args.use_backticks or args.enable_all,
        "random-backticks": args.random_backticks,
        "backticks-list": args.backticks,
        "hex-ip": args.hex_ip or args.enable_all,
        "random-type": args.randomization_type.lower(),
        "decimal": args.decimal,
        "base64": args.base64,
        "tfn-values": args.true_false_null,
        "safe": args.safe,
        "verbose": args.verbose
    }

    chameleon = Chameleon(filename=args.target, outfile=args.output, config=config, fmap=args.function_mapping)

    Console.auto_line(f"[+] Starting obfuscation at {datetime.utcnow()}")
    chameleon.obfuscate()
    chameleon.write_file()

    if args.check:
        Console.auto_line("  [#] Checking file against AMSI Trigger...")
        amsi = AMSITrigger()
        amsi.check(args.output)

    Console.auto_line(f"[+] Ended obfuscation at {datetime.utcnow()}\n")
