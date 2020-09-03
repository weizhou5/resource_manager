import base64
from Crypto.Cipher import AES


IV = bytes([0, 0, 0, 36, 0, 0, 0, 36, 0, 0, 0, 36, 0, 0, 0, 36])
AES_KEY = bytes([0, 0, 0, 36, 0, 0, 0, 36, 0, 0, 0, 36, 0, 0, 0, 36])

BS = len(AES_KEY)
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1:])]


class AESEncrypt(object):
    def __init__(self):
        self.key = AES_KEY
        self.mode = AES.MODE_CBC

    def decrypt(self, text):
        decode = base64.b64decode(text)
        cryptor = AES.new(self.key, self.mode, IV)
        plain_text = cryptor.decrypt(decode)
        return unpad(plain_text)

