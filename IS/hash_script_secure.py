import hashlib, sys, os

salt = os.urandom(32)		#generate secure random
password = sys.argv[1]		#first argument

key = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 200000)

print(key.hex())
