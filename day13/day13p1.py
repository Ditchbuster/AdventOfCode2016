import copy

inp = 1358
size = 100
maze = [None]*size
p = [1,1]
end = [39,31]
path =[]
print(maze)
def printMaze():
    global maze
    global size
    for x in range(size):
        row = ''.join(maze[x])
        print(row)
def move(to): #the point you are moving to
    global path
    path.append(to)
    
    if to == end:
        maze[to[0]][to[1]] = 'O'
        return True
    retn = []
    if to[0]+1 < size and maze[to[0]+1][to[1]] == '.':
        down = copy.copy(to)
        down[0] += 1
        if down not in path:
            retn.append(move(down))
    if to[1]+1 < size and maze[to[0]][to[1]+1] == '.':
        right = copy.copy(to)
        right[1] += 1
        if right not in path:
            retn.append(move(right))
    if to[0]-1 >= 0 and maze[to[0]-1][to[1]] == '.':
        up = copy.copy(to)
        up[0] -= 1
        if up not in path:
            retn.append(move(up))
    if to[1]-1 >= 0 and maze[to[0]][to[1]-1] == '.':
        left = copy.copy(to)
        left[1] -= 1
        if left not in path:
            retn.append(move(left))

    if True in retn:
        maze[to[0]][to[1]] = 'O'
        return True
    else:
        return False
        
for y in range(size):
    maze[y] = [' ']*size
    for x in range(size):
        tile = x*x + 3*x + 2*x*y + y + y*y + inp
        tile = bin(tile).count("1")
        if tile % 2 == 0:
            maze[y][x] = '.'
        else:
            maze[y][x] = '#'
move(p)
printMaze()
count = 0
for row in maze:
    count += row.count('O')
print(count-1)
    
