f = open('puzzle.txt')
for line in f:
    direction = 0 #0 north 1 east 2 south 3 west
    x = 0 #+north -south
    y = 0 #+east -west
    dis = 0

    #print(line, end='')
    path = line.split(', ')
    for turn in path:
        #print(turn[0])        
        if turn[0] == 'R':
            direction += 1
            if direction == 4:
                direction = 0
        if turn[0] == 'L':
            direction -= 1
            if direction == -1:
                direction = 3
        dis = int(turn[1:]) #get everything after the 0th char
        if direction == 0:
            x += dis
        elif direction == 1:
            y += dis
        elif direction == 2:
            x -= dis
        elif direction == 3:
            y -= dis

    print(str(abs(x) + abs(y)))
    #print(str(direction))
