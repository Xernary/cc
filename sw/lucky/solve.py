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
        r = remote("addr", 1337)

    return r


def main():
    r = conn()

    # good luck pwning :)
    
    data = r.recvuntil('Hi, what\'s your name? ')
    print(data)

    print(exe.symbols)
    print()
    print((exe.plt))
    print()
    print((exe.got))
    print(hex(exe.address))

    r.interactive()


if __name__ == "__main__":
    main()
