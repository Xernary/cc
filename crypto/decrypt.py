from Crypto.Cipher import DES
from Crypto.Util.Padding import *
from base64 import *

cipher = DES.new(bytes.fromhex('525c0be40e59ce62'), DES.MODE_CBC)
text = cipher.encrypt(pad('La lunghezza di questa frase non è divisibile per 8'.encode("utf8"), 8, style='x923'))
print("text = " + text.hex())
print("iv = " + b64encode(cipher.iv).decode('utf-8'))

#cipher = DES.new(bytes.fromhex('525c0be40e59ce62'), DES.MODE_CBC)
#text = unpad(cipher.decrypt('0000La lunghezza di questa frase non è divisibile per 8'.encode("utf8")), 8, style='x923')
#print(text)

