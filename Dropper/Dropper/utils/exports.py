# Marcus Botacin
# Generates export declarations from peframe JSONs

import sys  # get file
import json # assume file is a JSON

# Open file
_file = open(sys.argv[1],'r').read()
# Interpret as JSON
_json = json.loads(_file)
# Assume it is in PEFRAME format
for entry in _json['pe_info']['export_function']:
    # try to get function name
    function_name= entry['function']
    # Check if it is not none
    if function_name:
        # emit fake declaration
        # function does nothing, just returns
        print("extern \"C\" { __declspec(dllexport) void %s(){ return; }}" % function_name)

