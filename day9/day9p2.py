f = open("input.txt")
inp = ''
out = ''
for line in f:
    #print(line)
    if line[-1] == '\n':
        inp += line[:-1]
    else:
        inp += line
def calcSize( segment ):
    count = 0
    i = 0
    #print(segment)
    while i < len(segment):
        if segment[i] == '(':
            inst = ''
            x = 1
            while segment[i+x] != ')':
                x += 1
            inst = segment[i+1:i+x].split('x') # take the part inside () and split
            inst = [int(x) for x in inst]
            #print(segment[i+x+1:i+x+inst[0]+1])
            size = calcSize(segment[i+x+1:i+x+inst[0]+1])
            
            count += size*inst[1]
            i = i+inst[0]+x
        else:
            count += 1
        i += 1
    return count
print(calcSize(inp))
