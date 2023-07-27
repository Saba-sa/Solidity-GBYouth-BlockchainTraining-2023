import hashlib
with open('./2.1 Building Blocks - Hash structures, signatures, and coins.pptx','rb') as file:
    ppt=file.read()
    
with open('exa.pdf','rb') as file:
    pdf=file.read()

listOfHashes = []
listOfHashes2 = []

blockSize = len(ppt) // 1024
dataBlocks = [ppt[i:i + blockSize] for i in range(0, len(ppt), blockSize)]

blockSize = len(pdf) // 1024
dataBlocks_pdf = [pdf[i:i + blockSize] for i in range(0, len(pdf), blockSize)]

    
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
      
for x in range(len(dataBlocks_pdf)):
    stringHash = hashlib.sha256(dataBlocks_pdf[x]).hexdigest()
    listOfHashes2.append(stringHash)
    
listOfFiles=listOfHashes+listOfHashes2
finalMarkelRoot = makeMarkelTreeAndReturnMarkelRoot(listOfFiles)
print(f"Markel Root is:{finalMarkelRoot}")
