# Run
```
nasm -f macho64 {fileName for example mult_mem}.asm
ld -macosx_version_min 11.6.8 -o mult_mem mult_mem.o
./mult_mem
```
# The 80x86 CPU registers
- General-prupose registers
- special-purpose application-accessible registers
- Segment registers
- Special-prupose kernel-mode register