from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15

message='I\'m using RSA'
def generate_rsa():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypting_message(message, public_key):
    ciperText = public_key.encrypt(
        message.encode('utf-8'),
        padding.PKCS1v15()
    )
    return ciperText

def decrypt_message(CipherText, private_key):
    plaintext = private_key.decrypt(
        CipherText,
        padding.PKCS1v15()
    )
    return plaintext.decode('utf-8')


private_key, public_key = generate_rsa()
encrypted_message = encrypting_message(message, public_key)
decrypted_message = decrypt_message(encrypted_message, private_key)

print("Encrypted Message:", encrypted_message.hex())
print("Decrypted Message:", decrypted_message)

#DAS
from cryptography.hazmat.primitives.asymmetric import dsa
def  generateDSAKeyPair():
    private_key = dsa.generate_private_key(key_size=2048)
    public_key = private_key.public_key()
    return private_key,private_key

def DSASign(privateKey, message):
    sign = private_key.sign(
    message.encode(),
    hashes.SHA256()
    )
    return sign
def DSAVerify(publicKey, message, signature):
    try:
       public_key.verify(
        signature,
        message.encode(),
        hashes.SHA256()
        )
       return True
    except Exception:
        return False

private_key,public_key=generateDSAKeyPair()
signature=DSASign(private_key,message)
signature_varification=DSAVerify(public_key,message,signature)
if signature:
   print('varified')
else:
    print('not varified')
    