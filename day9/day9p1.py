f = open("input.txt")
inp = ''
out = ''
for line in f:
    #print(line)
    if line[-1] == '\n':
        inp += line[:-1]
    else:
        inp += line

i = 0
while i < len(inp):
    if inp[i] == '(':
        inst = ''
        x = 1
        while inp[i+x] != ')':
            x += 1
        inst = inp[i+1:i+x].split('x') # take the part inside () and split
        inst = [int(x) for x in inst] # make the parts ints
        #print(inst,i,x,inp[i+x+1:i+x+inst[0]+1])
        copy = inp[i+x+1:i+x+inst[0]+1]
        #print(copy)
        for k in range(inst[1]):
            out += copy
        #print(i,i+inst[0]+x)
        i = i+inst[0]+x
    else:
        out += inp[i]
    i += 1
print(inp)
print(out)
print(len(out))
