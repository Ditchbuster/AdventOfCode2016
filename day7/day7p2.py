import re
f = open("input.txt")
count = 0
for line in f:
    SSL = False
    parts = line.split(']')
    hyperList = []
    abbaList = []
    abaList = []
    for part in parts:
        part = part.split('[')
        if len(part)> 1:
            hyperList.append(part[1])
        abbaList.append(part[0])

    for abba in abbaList:
        for i in range(2,len(abba)):
            if abba[i] == abba[i-2] and abba[i] != abba[i-1]:
                #print (abba[i-2:i+1])
                abaList.append(abba[i-2:i+1])
    #print(abaList)
    for aba in abaList:
        bab = aba[1]+aba[0]+aba[1]
        #print(aba,bab)
        for hyper in hyperList:
            
            if bab in hyper:
                SSL = True
                break
        if SSL == True:
            break
    if SSL:
        count += 1
        
print(count)
            
