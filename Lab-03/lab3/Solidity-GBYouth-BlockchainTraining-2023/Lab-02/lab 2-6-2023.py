import bcrypt
import hashlib
from hashlib import sha256

name = input("Enter your name: ")
name_modified = name.encode('utf-8')
#md5
result = hashlib.md5(name_modified)
print('md5:',result.digest())
#sha1
result2 = hashlib.sha1(name_modified)
result2 = result2.hexdigest()
print('sha-1:',result2)

#sha256
result3 = sha256(name_modified).hexdigest()
print('sha-256:',result3)

#sha512
result4 = hashlib.sha512(name_modified)
result4 = result4.hexdigest()
print('sha-512:',result4)

#sha3
result5 = hashlib.sha3_224(name_modified)
result5 = result5.hexdigest()
print('sha-3:',result5)

# BLAKE2
blake2_hash = hashlib.blake2b(name_modified).hexdigest()
print('BLACKE2:',blake2_hash)

#bcrypt
salt = bcrypt.gensalt()
result6 = bcrypt.hashpw(name_modified, salt)
print('bcrypt:',result6)
#ripemd160
result7=hashlib.new('ripemd160')
result7.update(name_modified)
haxh=result7.hexdigest()
print('ripemd160:',haxh)