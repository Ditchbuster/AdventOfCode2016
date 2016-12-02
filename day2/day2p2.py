f = open('input.txt')
size = 4
p = [2,0]
code = []
keypad = [['0','0','1','0','0'],['0','2','3','4','0'],['5','6','7','8','9'],['0','A','B','C','0'],['0','0','D','0','0']]
for line in f:
    #print(line)
    for c in line:
        #print(c)
        if c == 'U':
            #print(str(p[0]))
            if p[0]-1 >= 0 and keypad[p[0]-1][p[1]] != '0':
                p[0] -= 1
        if c == 'D':
            if p[0]+1 <= size and keypad[p[0]+1][p[1]] != '0':
                p[0] += 1
        if c == 'L':
            if p[1]-1 >= 0 and keypad[p[0]][p[1]-1] != '0':
                p[1] -= 1
        if c == 'R':
            if p[1]+1 <= size and keypad[p[0]][p[1]+1] != '0':
                p[1] += 1
    code.append(keypad[p[0]][p[1]])
print (code)
