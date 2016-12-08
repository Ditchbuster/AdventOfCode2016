f = open("input.txt")
screen = [['.' for _ in range(50)] for _ in range(6)] #row first
#print(screen)
for line in f:
    parts = line.split()
    if parts[0] == 'rect':
        rect = parts[1].split('x')
        #print(rect)
        for x in range(int(rect[1])):
            for y in range(int(rect[0])):
                screen[x][y] = '#'
    if parts[0] == 'rotate':
        if parts[1]=='row':
            row = parts[2].split('=')
            row = int(row[1])
            shift = int(parts[4])
            #temp = []
            temp=screen[row][-shift:]
            #print(temp)
            temp.extend(screen[row][:-shift])
            #print(temp)
            #print (''.join(screen[row]))
            #print (''.join(str(x) for x in temp))
            screen[row] = ''.join(str(x) for x in temp)
        if parts[1]=='column':
            colm = parts[2].split('=')
            colm = int(colm[1])
            shift = int(parts[4])
            temp = []
            for i in range(shift,len(screen))
                temp.append(screen[i])
            temp=screen[-shift:][colm]
            print(temp)
            temp.extend(screen[row][:-shift])
            print(temp)
            #print (''.join(screen[row]))
            #print (''.join(str(x) for x in temp))
            screen[row] = ''.join(str(x) for x in temp)
                
                


for r in screen:
    print(''.join(r))
        
