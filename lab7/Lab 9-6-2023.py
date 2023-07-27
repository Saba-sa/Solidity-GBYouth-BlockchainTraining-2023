from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

def generateECDSKeyPair():
    private_key = ec.generate_private_key(ec.SECP256K1())
    public_key = private_key.public_key()
    return private_key, public_key

def ECDSASign(private_key, message):
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA3_256())
    )
    return signature

def ECDSVerify(public_key, message, signature):
    try:
        public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except:
        return False

def main():
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSKeyPair()
    message = b'Message for ECDSA algorithm'
    signature = ECDSASign(ECDSAPrivateKey, message)
    verification = ECDSVerify(ECDSAPublicKey, message, signature)

    print(ECDSAPublicKey)
    print(ECDSAPrivateKey)
    print(message.decode())
    print(signature)
    print(verification)

main()
