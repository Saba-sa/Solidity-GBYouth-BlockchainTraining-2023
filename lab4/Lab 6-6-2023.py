import hashlib
partA='1d0ada7a906e529d19fb2aca66911eaaee84ff4c7c6b685f019cd79c2deec5ff'
partB='6c8ed1b6a6745bc64645ce63e23c9258545de0bf1c3c8efdfb3fad46d5d1fb6c'
partC='c43194ab05fca649152ea3b92c49eacee99902badd7ea503e3315d49a83781ba'
partD='b349939cb094a89e4cf720b895df300c0d5c7b3f0f3a237bc026cad42637fb61'



conAB=partA+partB
conCD=partC+partD

hashAB = hashlib.sha256(conAB.encode('utf-8')).hexdigest()
hashCD = hashlib.sha256(conCD.encode('utf-8')).hexdigest()

conABCD=hashAB+hashCD

hashABCD=hashlib.sha256(conABCD.encode('utf-8')).hexdigest()

print('H(X)=H(H(A)+H(B)):',hashAB)
print('H(Y)=H(H(C)+H(D)):',hashCD)
print('H(H(X)+H(Y)):',hashABCD)
#question 2
eightStr=['The fox jumps','DJs flock by ax quiz prog. Junk MTV quiz whelp','verx zippy fowls. Few quips he moc','quick, brown ','when MTV','galvanized t','y bad quack might jin','graced by fox']

hashEight1 = hashlib.sha256(eightStr[0].encode('utf-8')).hexdigest()
hashEight2 = hashlib.sha256(eightStr[1].encode('utf-8')).hexdigest()
hashEight3 = hashlib.sha256(eightStr[2].encode('utf-8')).hexdigest()
hashEight4 = hashlib.sha256(eightStr[3].encode('utf-8')).hexdigest()
hashEight5 = hashlib.sha256(eightStr[4].encode('utf-8')).hexdigest()
hashEight6 = hashlib.sha256(eightStr[5].encode('utf-8')).hexdigest()
hashEight7 = hashlib.sha256(eightStr[6].encode('utf-8')).hexdigest()
hashEight8 = hashlib.sha256(eightStr[7].encode('utf-8')).hexdigest()
 
con12=hashEight1+hashEight2
con34=hashEight3+hashEight4
con56=hashEight5+hashEight6
con78=hashEight7+hashEight8

hash12 = hashlib.sha256(con12.encode('utf-8')).hexdigest()
hash34 = hashlib.sha256(con34.encode('utf-8')).hexdigest()
hash56 = hashlib.sha256(con56.encode('utf-8')).hexdigest()
hash78 = hashlib.sha256(con78.encode('utf-8')).hexdigest()

con1234=hash12+hash34
con5678=hash56+hash78

hash1234 = hashlib.sha256(con1234.encode('utf-8')).hexdigest()
hash5678 = hashlib.sha256(con5678.encode('utf-8')).hexdigest()

rootCon=hash1234+hash5678
rootHash=hashlib.sha256(rootCon.encode('utf-8')).hexdigest()

print('\nroothash is:',rootHash)

#question 3
with open('./2.1 Building Blocks - Hash structures, signatures, and coins.pptx','rb') as file:
    ppt=file.read()

listOfHashes = []

blockSize = len(ppt) // 1024
dataBlocks = [ppt[i:i + blockSize] for i in range(0, len(ppt), blockSize)]

    
def makeMarkelTreeAndReturnMarkelRoot(data):
    treeHashes = data
    while (len(treeHashes) > 1):
        newHashs = []
        if (len(treeHashes) % 2 != 0):
            treeHashes.append(treeHashes[len(treeHashes) - 1])

        for y in range(0, len(treeHashes), 2):
            firstHash = treeHashes[y]
            secondhash = treeHashes[y + 1]
            concatinatedHashes = firstHash + secondhash
            hashOfConcatinatedHashes = hashlib.sha256(concatinatedHashes.encode()).hexdigest()
            newHashs.append(hashOfConcatinatedHashes)

        treeHashes = newHashs

    return treeHashes[0]

for x in range(len(dataBlocks)):
    stringHash = hashlib.sha256(dataBlocks[x]).hexdigest()
    listOfHashes.append(stringHash)
      
finalMarkelRoot = makeMarkelTreeAndReturnMarkelRoot(listOfHashes)
print(f"Markel Root is:{finalMarkelRoot}")
