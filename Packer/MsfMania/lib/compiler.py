from lib import core
from os import system, chdir
from subprocess import check_call, PIPE
from random import randint
from hashlib import sha256, md5


def auto_compile(filename, architecture, icon, require_admin):
    compiler = []
    if architecture == "x64":
        compiler += ["x86_64-w64-mingw32-windres", "x86_64-w64-mingw32-gcc"]
    else:
        compiler += ["i686-w64-mingw32-windres", "i686-w64-mingw32-gcc"]

    rc = ""
    if icon != "":
        rc += 'id ICON "icon/' + ''.join((icon, '"\n'))
        rc += rc_info_maker(filename, require_admin)
    else:
        rc += rc_info_maker(filename, require_admin)

    with open('tmp/MsfMania.rc', 'w') as f:
        f.write(rc)

    system(f"{compiler[0]} tmp/MsfMania.rc -O coff -o tmp/MsfMania.res && {compiler[1]} tmp/source.c tmp/MsfMania.res -Wl,-Bstatic -lpsapi -static -s -w -o {filename} && rm -rf tmp/")
    core.compilation_completed()


def upx(filename):
    filename = filename.replace("output/", "")
    chdir("output/")
    # use "--ultra-brute" or "--lzma"
    system(f"upx --ultra-brute {filename} --compress-icons=1 -qqq")
    core.pe_packed()
    chdir("..")


def rar(filename):
    chdir("output/")
    archive = filename.replace('.exe', '.rar')
    archive = archive.replace('output/', '')
    filename = filename.replace('output/', '')
    compress = ['rar', 'a', '-m5', archive, filename]
    check_call(compress, stdout=PIPE)
    core.rar_compressed()
    chdir("..")


def hash_file(filename, algo_hash):
    if algo_hash == "sha256":
        hash_type = "SHA256"
        hash_sha256 = sha256()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
            core.file_hash(hash_type, hash_sha256.hexdigest())

    elif algo_hash == "md5":
        hash_type = "MD5"
        hash_md5 = md5()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
            core.file_hash(hash_type, hash_md5.hexdigest())


def rc_info_maker(filename, require_admin):
    rc_info = ""

    if require_admin == "yes":
        filename = filename.replace("output", "tmp") + '.manifest"'
        rc_info += '1 MANIFEST "' + filename + "\n"
        admin_privs(filename)

    rc_info += "1 VERSIONINFO\n"
    rc_info += f"FILEVERSION     {str(rc_version())},{str(rc_version())}\n"
    rc_info += f"PRODUCTVERSION  {str(rc_version())},{str(rc_version())}\n"
    rc_info += "BEGIN\n" + 'BLOCK "StringFileInfo"\n'
    rc_info += "BEGIN\n"
    rc_info += 'BLOCK "080904E4"\n'
    rc_info += 'BEGIN\n'
    rc_info += f'VALUE "CompanyName", "{str(core.varname_creator())}"\n'
    rc_info += f'VALUE "FileDescription", "{str(core.varname_creator())}"\n'
    rc_info += f'VALUE "FileVersion", "{str(rc_version())}.{str(rc_version())}"\n'
    rc_info += f'VALUE "InternalName", "{str(core.varname_creator())}"\n'
    rc_info += f'VALUE "LegalCopyright", "{str(core.varname_creator())}"\n'
    rc_info += f'VALUE "OriginalFilename", "{str(core.varname_creator())}"\n'
    rc_info += f'VALUE "ProductName", "{str(core.varname_creator())}"\n'
    rc_info += f'VALUE "ProductVersion", "{str(rc_version())}.{str(rc_version())}"\n'
    rc_info += 'END\n'
    rc_info += 'END\n'
    rc_info += 'BLOCK "VarFileInfo"\n'
    rc_info += 'BEGIN\n'
    rc_info += 'VALUE "Translation", 0x809, 1252\n'
    rc_info += 'END\n'
    rc_info += 'END\n'
    return rc_info


def rc_version():
    var_rc_version = str(randint(1, 9999999))
    return var_rc_version


def admin_privs(filename):
    manifest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    manifest += '<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">\n'
    manifest += '<trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">\n'
    manifest += '<security>\n'
    manifest += '<requestedPrivileges>\n'
    manifest += '<requestedExecutionLevel level="requireAdministrator" uiAccess="false"/>\n'
    manifest += '</requestedPrivileges>\n'
    manifest += '</security>\n'
    manifest += '</trustInfo>\n'
    manifest += '</assembly>\n'

    filename = filename.replace('"', '')
    with open(filename, 'w') as f:
        f.write(manifest)
