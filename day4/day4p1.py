f = open("input.txt")
sector = 0

for line in f:
    letters = [0] * 26    
    parts = line.split('-')
    checksum = parts[-1].split("[") #actually sector id and checksum
    parts = parts[:-1] #trim off checksum and sector id
    if checksum[-1][-1] == '\n':
        checksum[-1] = checksum[-1][:-2]
    else:
        checksum[-1] = checksum[-1][:-1]

    for p in parts:
        for c in p:
            letters[ord(c)-97] += 1
    vaild = True
    for c in checksum[1]:
        if letters.index(max(letters)) == ord(c)-97:
            letters[ord(c)-97] = -1
        else:
            vaild = False
            break
    if vaild == True:
        sector += int(checksum[0])
    
    #print(letters)

print(sector)
    
