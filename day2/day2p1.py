f = open('input.txt')
size = 3
p = [1,1]
code = []
for line in f:
    print(line)
    for c in line:
        print(c)
        if c == 'U':
            print(str(p[0]))
            p[0] -= 1
            if p[0] < 0:
                p[0] = 0
        if c == 'D':
            p[0] += 1
            if p[0] > size - 1:
                p[0] = size - 1
        if c == 'L':
            p[1] -= 1
            if p[1] < 0:
                p[1] = 0
        if c == 'R':
            p[1] += 1
            if p[1] > size - 1:
                p[1] = size - 1
    code.append(str(p))
print (code)
