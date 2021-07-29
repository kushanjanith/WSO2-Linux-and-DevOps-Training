import hashlib, sys, os

salt = os.urandom(32)				#generate secure random
password = (sys.argv[1]).encode("utf-8")	#first argument

SHA512 = hashlib.sha512(salt+password).hexdigest()

print(SHA512)
