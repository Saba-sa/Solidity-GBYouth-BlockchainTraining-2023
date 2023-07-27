from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
import hashlib
import random

def randomNo(start,end):
    return random.randint(start,end)


def generateTxid():
    return hashlib.sha256(str(randomNo(0, 1000)).encode()).hexdigest()

def generateInput():
    prevTxid=generateTxid()
    prevOutputIndex=randomNo(1,5)
    return prevTxid,prevOutputIndex

def generateOutput():
    recipientAddress = 'recipient_address_'+str(randomNo(1,100))
    amount=round(random.uniform(0.001, 1.0), 8)
    return recipientAddress,amount

def generateTransactionFee():
    return round(random.uniform(0.0001 ,0.001),8)

def generateRandomTransaction():
    txid = generateTxid()
    inputPrevTxid, inputPrevOutputIndex =generateInput()
    outputRecipientAddress, outputAmount =generateOutput()
    transactionFee = generateTransactionFee()
    return txid,inputPrevTxid,inputPrevOutputIndex,outputRecipientAddress,outputAmount,transactionFee

def concatenateString(txid, inputPrevTxid,inputPrevOutputIndex, outputRecipientAddress,outputAmount, transactionFee):
    transactionData = f"{str(txid)}{str(inputPrevTxid)}{str(inputPrevOutputIndex)}{str(outputRecipientAddress)}{str(outputAmount)}{str(transactionFee)}"
    return transactionData

def generateECDSAKeyPair():
    ECDSAPrivateKey = ec.generate_private_key(ec.SECP256K1())
    ECDSAPublicKey=ECDSAPrivateKey.public_key()
    return ECDSAPrivateKey,ECDSAPublicKey

def  ECDSASign(privateKey, message):
    signature = privateKey.sign(message, ec.ECDSA(hashes.SHA256()))
    return signature

def  ECDSAVerify(publicKey, message,signature):
    try:
        publicKey.verify(signature,message,ec.ECDSA(hashes.SHA256()))
        return True
    except:
        return False
    
def main():
    txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee = generateRandomTransaction()
    transactionDataAsMessage = concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee).encode()
    EDCSAPrivateKey, EDCSAPublicKey = generateECDSAKeyPair()
    signature = ECDSASign(EDCSAPrivateKey, transactionDataAsMessage)
    verified = ECDSAVerify(EDCSAPublicKey, transactionDataAsMessage, signature) 

    print("\n")
    print("PRINT ECDSA DETAILS")
    print("\n")
    print(f"ECDSA Public Key: {EDCSAPublicKey}")
    print(f"ECDSA Private Key: {EDCSAPrivateKey}")
    print(f"Transaction Data Message: {transactionDataAsMessage}")
    print(f"Signature: {signature}")
    print(f"Verification: {verified}")
    print("\n")

main()