nasm -f elf32 -o code.o code.asm
ld -m elf_i386 -o code code.o
