import hashlib
import base58
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization



def generateECDSA():
    ECDSAPrivateKey = ec.generate_private_key(ec.SECP256K1())
    ECDSAPublicKey = ECDSAPrivateKey.public_key()
    return ECDSAPrivateKey, ECDSAPublicKey


def bitcoinWalletAddress(ECDSAPublicKey):

    sha256hash = hashlib.sha256(ECDSAPublicKey).hexdigest()
    
    Ripemd160Hash = hashlib.new('ripemd160', sha256hash.encode()).digest()

    net_ripemd_hash = b'00' + Ripemd160Hash

    shaHashOfRipemd160 = hashlib.sha256(Ripemd160Hash).hexdigest()
    version_shaHashOfRipemd160 = hashlib.sha256(shaHashOfRipemd160.encode()).hexdigest()
    
    checksum = version_shaHashOfRipemd160[:8]
    base = checksum + version_shaHashOfRipemd160
    address = base58.b58encode(base)

    print("sha:", sha256hash)
    print("ripe:", Ripemd160Hash)
    print("sha2256 of ripe:", shaHashOfRipemd160)
    print("version_shahash of ripe:", version_shaHashOfRipemd160)
    print("address:", address.decode())
    

    return address


ECDSAPrivateKey, ECDSAPublicKey = generateECDSA()
publicKeyBytes = ECDSAPublicKey.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint)
bitcoinWalletAddress(publicKeyBytes)