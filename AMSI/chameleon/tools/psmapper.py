import json
import os
import secrets
import string
import sys
import re
from enum import Enum
import argparse


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
        self.ctx.pop()
        return self.current

    @property
    def balanced(self) -> bool:
        if not self.is_empty():
            return self.ctx[-1].brackets == 0

    def is_empty(self):
        return len(self.ctx) == 0

    def close(self):
        self.ctx.pop()

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
            matches.append(e)
        matches.sort(key=len)
        return matches[::-1]

    def to_string(self):
        return "->".join([self.ctx[i].ctx_type.name for i in range(len(self.ctx))])


def scramble(text):
    new_text = ""
    for char in text:
        if char.islower():
            new_text += secrets.choice(string.ascii_lowercase)
        else:
            new_text += char
    return new_text


def replace_comments(text):
    # Get rid of <# ... #> comments
    _content = text.encode().decode(encoding="windows-1252", errors="replace")
    start = False
    matches = re.finditer(r"<#[^#]+#>", _content, re.MULTILINE)
    for _, match in enumerate(matches, start=1):
        _content = _content.replace(match.group(), "")

    text = _content.split("\n")

    rows = []
    for nr, row in enumerate(text, start=1):
        if row.find("<#") > -1:
            start = True
        if row.find("#>") > -1:
            start = False
        if not start:
            rows.append(row)

    _content = "\n".join(rows)

    # Single Line Comments
    slc_pattern = re.compile(r"#.+")
    matches = slc_pattern.finditer(_content)
    for _, match in enumerate(matches, start=1):
        _content = _content.replace(match.group(), "")
    return _content


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Chameleon PSMapper - Helper to create obfuscated function mappings'
    )
    parser.add_argument('-o', '--outfile', required=True, type=str, default=None, help='Output file')
    parser.add_argument('target', help='Target PS1 script')

    args = parser.parse_args()

    if not os.path.isfile(args.target):
        print(f"[-] File {args.target} not found")
        sys.exit(1)

    with open(args.target, "r") as ps:
        content = ps.read()

    content = replace_comments(content)
    content = content.split("\n")

    tree = PSTree(
        psctx=PSContext(name="main", ctx_type=PSContextType.MAIN)
    )

    mapping = {}
    function = ""

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
                    print(f"Found new function {function} at line: {n}")
                    tree.change_context(ctx_name=function, ctx_type=PSContextType.FUNCTION)
                    see_next = True
                elif tree.current_ctx_type == PSContextType.FUNCTION:
                    print(f"Found new nested function {function} at line: {n}")
                    tree.change_context(ctx_name=function, ctx_type=PSContextType.NESTED_FUNCTION)
                    see_next = True
                ob = line.count("{")
                if ob == 0:
                    see_next = True
                else:
                    print(f"Function starts at line: {n}")
                cb = line.count("}")
            elif param_match:
                tree.change_context(ctx_name=tree.current.name + "-param", ctx_type=PSContextType.PARAMS)
                ob = line.count("(")
                cb = line.count(")")
                if ob == 0:
                    see_next = True
                else:
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
                print(f"  > Found parameters: {params}")
                mapping[function] = params
                # Close parameters context
                print(f"Param() close at line {n}")
                tree.close()
            elif tree.current_ctx_type == PSContextType.NESTED_FUNCTION:
                # Close function context
                print(f"Nested function closes at line {n}")
                tree.close()
            elif tree.current_ctx_type == PSContextType.FUNCTION:
                # Close function context
                print(f"Function closes at line {n}")
                tree.close()

    new_mapping = {}
    for k, v in mapping.items():
        new_params = {}
        new_params["original"] = v
        new_params["repl"] = [scramble(param) for param in v]

        new_mapping[k] = {
            "repl": scramble(k),
            "params": new_params
        }

    with open(args.outfile, 'w') as outfile:
        json.dump(new_mapping, outfile)

    json_formatted = json.dumps(new_mapping, indent=2)
    # print(json_formatted)
