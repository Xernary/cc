#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *


def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "software-17.challs.olicyber.it"
    PORT = 13000
    r = remote(HOST, PORT)

    # .send() può essere invocato sull'oggetto ritornato da remote() per inviare dati
    #r.send(b"Ciao!")

    # .sendline() è identico a .send(), però appende un newline dopo i dati
    #r.sendline(b"Ciao!")

    # .sendafter() e .sendlineafter() inviano la stringa "Ciao!"
    #r.sendafter(b"... Invia un qualsiasi carattere per iniziare ...", b"k")

    # solo dopo che viene ricevuta la stringa "something"
    r.sendlineafter(b"... Invia un qualsiasi carattere per iniziare ...", b"k")

    # .recv() riceve e ritorna al massimo 1024 bytes dalla socket
    #data = r.recv(1024)
    #print(data)

    # .recvline() legge dalla socket fino ad un newline
    data = r.recvline()

    for i in range(10):
        data = r.recvline()
        print(data)
        #data_bytes = str.encode(data)
        data_str = str(data, 'UTF8')
        data_str = data_str.replace("[", "")
        data_str = data_str.replace("]", "")
        print(type(data_str))
        print(data_str)
        data_int = list(map(int, (data_str.split(", "))))
        print(data_int)
        sum = 0
        for i in data_int:
            sum += i
        print(sum)
        r.sendlineafter(b"Somma? : ", str(sum))
        data = r.recvline()

    print(data)
    r.recvline()
    print(data)

    # .recvuntil() legge dalla socket finchè non viene incontrata la stringa "something"
    #data = r.recvuntil(b"something")

    # permette di interagire con la connessione direttamente dalla shell
    #r.interactive()

    # chiude la socket
    r.close()


if __name__ == "__main__":
    main()
