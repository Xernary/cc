#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *
from binascii import hexlify


def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "piecewise.challs.cyberchallenge.it"
    PORT = 9110
    r = remote(HOST, PORT)

    # .send() può essere invocato sull'oggetto ritornato da remote() per inviare dati
    #r.send(b"Ciao!")

    # .sendline() è identico a .send(), però appende un newline dopo i dati
    #r.sendline(b"Ciao!")

    # .sendafter() e .sendlineafter() inviano la stringa "Ciao!"
    #r.sendafter(b"... Invia un qualsiasi carattere per iniziare ...", b"k")


    # .recvuntil() legge dalla socket finchè non viene incontrata la stringa "something"

    while 1:
        string = r.recvline()
        print(string)
        data = string.decode("utf-8")
        result = b'\x00'
        if "Please send me the number" in data:
            number = int(data.split(" ")[5])
            bits = int((data.split(" ")[8])[:2])
            print("BITS = " + str(bits))
            print("NUMBER = " + str(number))
            if "little-endian" in data:
                #little endian
                result = number.to_bytes(int(bits/8), 'little') 
            else:
                #big endian
                result = number.to_bytes(int(bits/8), 'big') 
            print(hexlify(result))
            r.send(result)
        elif "empty line" in data:
            r.send(b'\n')

        print(r.recvline())





    # permette di interagire con la connessione direttamente dalla shell
    #r.interactive()

    # chiude la socket
    #r.close()


if __name__ == "__main__":
    main()
