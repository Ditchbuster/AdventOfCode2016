import re
f = open("input.txt")
count = 0
for line in f:
    TLS = False
    parts = line.split(']')
    hyperList = []
    abbaList = []
    for part in parts:
        part = part.split('[')
        if len(part)> 1:
            hyperList.append(part[1])
        abbaList.append(part[0])

    for abba in abbaList:
        if re.search(r'(.)(.(?!\1))\2\1',abba) != None:
            TLS = True
            break
    for hyper in hyperList:
        if re.search(r'(.)(.(?!\1))\2\1',hyper) != None:
            TLS = False
            break
    if TLS:
        count += 1
        
print(count)
            
