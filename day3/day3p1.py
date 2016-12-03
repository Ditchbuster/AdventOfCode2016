f = open("input.txt")
vaild = 0
invaild = 0
lines = 0
for line in f:
    lines += 1
    sides = line.split()
    
    for i in range(len(sides)):
        sides[i] = int(sides[i])

    if sides[0]+sides[1] > sides[2] and sides[0]+sides[2] > sides[1] and sides[2]+sides[1] > sides[0]:
        vaild += 1
    #maxSide = max(sides)
    #others = 0
    #for s in sides:
    #    if s != maxSide:
    #        others += s
    #
    #if others > maxSide:
    #    vaild += 1
    #else:
    #   invaild += 1
    #print(sides,others,maxSide,vaild)
print(vaild, invaild,  lines)
    
