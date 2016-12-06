f = open("input.txt")
spot = [0]*26
mesg = []

for line in f:
    while len(mesg) < len(line):
        #print('adding spot')
        mesg.append(spot.copy())
    for i in range(len(line)):
        #print(line[i])
        if(line[i].isalpha()):
            mesg[i][ord(line[i])-97] += 1

for s in mesg:
    print(chr(s.index(min(s))+97))
