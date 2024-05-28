section .text
global _start

_start:

    mov ebx, hello
    mov eax, 0xb
    mov ecx, 0x0
    mov edx, 0x0
    mov esi, eip
    mov ebx, [esi+3]
    int 0x80
    nop

section .data
    hello db "/bin/sh", 0x0
    helloLen equ $-hello





