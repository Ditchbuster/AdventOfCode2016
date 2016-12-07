f = open("input.txt")
count = 0
for line in f:
    TLS = False
    last = ''
    sbrack = line.index('[')
    ebrack = line.index(']')
    brack = line[sbrack:ebrack]
    line = line[:sbrack]+line[ebrack:]
    print(line,brack)
    for i in range(len(line)):
        #print(line[i])
        if i+1 == len(line):
            break
    
        if i < 2:
            last = line[i]
            continue
        
        if line[i] == last:
            if line[i-2] == line[i+1] and line[i]!= line[i+1]:
                TLS = True
                break
        print(line[i],last)
        last = line[i]

    for i in range(len(brack)):
        #print(line[i])
        if i+1 == len(brack):
            break
    
        if i < 2:
            last = brack[i]
            continue
        
        if brack[i] == last:
            if brack[i-2] == brack[i+1] and brack[i]!= brack[i+1]:
                TLS = False
                break
        print(brack[i],last)
        last = brack[i]
        
    if TLS==True:
        count += 1
        print('ture')
print(count)
            
