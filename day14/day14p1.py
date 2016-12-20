import hashlib
import re
inp='abc'
inp = 'zpqevtbw'
myHashes = []
keys = []
for x in range(40000):
    has = inp + str(x)
    myHashes.append(hashlib.md5(has.encode('utf-8')).hexdigest())

for i in range(len(myHashes)-1000):
    m = re.search(r'(.)\1\1',myHashes[i])
    if m != None:
        #print(m.group(0))
        char = m.group(0)[0]
        s = r'('+char+r'){5}'
        #print(s)
        for x in range(i+1,i+1001):
            k = re.search(s,myHashes[x])
            if k != None:
                keys.append(i)
                print(len(keys),i,x,s,m.group(0),k.group(0),myHashes[i],myHashes[x])
                break


for h in keys:
    print(h)
if len(keys)>64:
    print('64th key index: ' + str(keys[63]))
            
