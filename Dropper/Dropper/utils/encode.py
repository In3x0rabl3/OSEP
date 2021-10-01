# Marcus Botacin
# Encode a C string in an int array

# Get input
import sys
# Consider each input char + '\0'
input = sys.argv[1]+'\0'
# encode (in this case, simply considering the ascii value)
x = ','.join(["%d" % ord(c) for c in input])
# produce the array declaration
print("int x[] ={"+x+"};")
# produce the invocation of the decode function
print("decode(x,%d);" % len(input))
