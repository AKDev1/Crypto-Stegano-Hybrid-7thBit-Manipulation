# from Crypto.Cipher import AES
import base64

# cipher = AES.new('dcsnfvrwfejkdsvfdnbfwejqdkcvfndbgenrfwevkdfnbgnerfwemkvfbgetngrfe',AES.MODE_ECB) # never use ECB in strong systems obviously
# encoded = base64.b64encode(cipher.encrypt('aman'))
# print(encoded)
# # ...
# decoded = cipher.decrypt(base64.b64decode('aman'))
# print(decoded)

# import base64
# import hashlib
# from Crypto import Random
# from Crypto.Cipher import AES

# class AESCipher(object):

#     def __init__(self, key): 
#         self.bs = AES.block_size
#         self.key = hashlib.sha256(key.encode()).digest()

#     def encrypt(self, raw):
#         raw = self._pad(raw)
#         iv = Random.new().read(AES.block_size)
#         cipher = AES.new(self.key, AES.MODE_CBC, iv)
#         return base64.b64encode(iv + cipher.encrypt(raw.encode()))

#     def decrypt(self, enc):
#         enc = base64.b64decode(enc)
#         iv = enc[:AES.block_size]
#         cipher = AES.new(self.key, AES.MODE_CBC, iv)
#         return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

#     def _pad(self, s):
#         return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

#     @staticmethod
#     def _unpad(s):
#         return s[:-ord(s[len(s)-1:])]



# def base64_e():
# 	try:
# 		decoded_string = input('String To Encode: ')
# 		encoded_string = base64.b64encode(decoded_string.encode('ascii'))
# 		print (encoded_string.decode('ascii'))
# 		print()
# 	except:
# 		print(' Invalid Input')

# def base64_d():
# 	try:
# 		encoded_string = input('Encoded String : ')
# 		decoded_string = base64.b64decode(encoded_string.encode('ascii'))
# 		print (decoded_string.decode('ascii'))
# 		print()
# 	except:
# 		print(' Invalid Input')

# base64_d()
import binascii

msg1  = b'aman'
print(msg1)
y = 'aman'
msg = y.encode('UTF-8')
print(msg)