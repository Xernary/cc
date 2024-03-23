#!/usr/bin/env python3

from base64 import b64decode
s = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE='
print(b64decode(s))
c = 664813035583918006462745898431981286737635929725
n = (c).to_bytes((c.bit_length() + 7), byteorder='big')
print(n)
