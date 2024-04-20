import zlib

fh = open('plz_with_offset', 'rb')
cdata = fh.read()

zlib.decompress(cdata, zlib.MAX_WBITS|16)

fh.close()

zlibd()
