import hashlib
with open('exa.pdf', 'rb') as file:
    binary_data = file.read()

online_Value='c27783392976304d9ec296c6cf318f4145e780d02b78c679347e93408553a59c'

def compute_sha256(data):
    sha256_hash = hashlib.sha256(data).hexdigest()
    return sha256_hash

sha256 = compute_sha256(binary_data)

def conditionChecker(x, y):
    if x == y:
        return 'equal'
    else:
        return 'not equal'
result = conditionChecker(sha256,online_Value)
print(result)  

#Another file
randOnlineVal='dddfc0afca8f434ea99bc2751d41fe3f995731aec1798920b6dd50a390bfb073'

with open('randExa.pptx', 'rb') as file:
    binary_data_rand = file.read()

rand=compute_sha256(binary_data_rand)

result2 =conditionChecker(rand,randOnlineVal)
print(result2)  

#Calculation MD5 and SHA1
with open('message1.bin','rb') as file:
    msg1=file.read()
with open('message2.bin','rb') as file:
    msg2=file.read()
  
#md5
def compute_md5(data):
    md5_hash = hashlib.md5(data).hexdigest()
    return md5_hash

md5msg1 = compute_md5(msg1)
md5msg2 = compute_md5(msg2)
print('md5 of msg1:',md5msg1)
print('md5 of msg2:',md5msg2)

#sha1
def compute_md1(data):
    md5_hash = hashlib.sha1().hexdigest()
    return md5_hash

md5msg1 = compute_md1(msg1)
md5msg2 = compute_md1(msg2)

print('sha1 of msg1:',md5msg1)
print('sha1 of msg2:',md5msg2)
