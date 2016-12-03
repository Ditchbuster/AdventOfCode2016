f = open("input.txt")
vaild = 0
invaild = 0
lines = 0
i = 0
sides = []
for line in f:
    lines += 1
    sides.append(line.split()) 
    for d in range(3):
        sides[i][d] = int(sides[i][d])

    if i == 2:
        print(sides)
        for x in range(3):
            a = sides[0][x]
            b = sides[1][x]
            c = sides[2][x]
            print(a,b,c)
            if a+b > c and a+c > b and b+c > a:
                vaild += 1
        sides = []
        i = 0
    else:
        i += 1
print(vaild, invaild,  lines)
    
