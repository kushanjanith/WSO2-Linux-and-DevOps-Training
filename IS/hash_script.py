import hashlib, sys

salt = b'Km5d5ivMy8iexuHcZrsD'  #byte value of the salt
password = sys.argv[1]		#first argument

key = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 200000)

print(key.hex())
