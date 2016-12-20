import copy
from queue import Queue

inp = 1358
size = 100
maze = [None]*size


def printMaze():
    global maze
    global size
    for x in range(size):
        row = ''.join(maze[x])
        print(row)

def neighbors(point):
    to = [point.y,point.x]
    global maze
    global size
    retn = []
    if to[0]+1 < size and maze[to[0]+1][to[1]] == '.':
        down = copy.copy(to)
        down[0] += 1
        retn.append(down)
    if to[1]+1 < size and maze[to[0]][to[1]+1] == '.':
        right = copy.copy(to)
        right[1] += 1
        retn.append(right)
    if to[0]-1 >= 0 and maze[to[0]-1][to[1]] == '.':
        up = copy.copy(to)
        up[0] -= 1
        retn.append(up)
    if to[1]-1 >= 0 and maze[to[0]][to[1]-1] == '.':
        left = copy.copy(to)
        left[1] -= 1
        retn.append(left)
    retn = [myTile(r[0],r[1]) for r in retn]
    return retn

for y in range(size):
    maze[y] = [' ']*size
    for x in range(size):
        tile = x*x + 3*x + 2*x*y + y + y*y + inp
        tile = bin(tile).count("1")
        if tile % 2 == 0:
            maze[y][x] = '.'
        else:
            maze[y][x] = '#'
class myTile(object):
    def __init__(self,y=0,x=0,frm = None):
        self.x = x
        self.y = y
        self.frm = frm
    def __eq__(self,other):
        if not isinstance(other, myTile):
            return False
        if self.x != other.x or self.y != other.y:
            return False
        return True
    def __hash__(self):
        return hash((self.y,self.x))

start = myTile(1,1)
end = [39,31]
path =[]

frontier = Queue()
frontier.put(start)
visited = []
visited.append(start)
while not frontier.empty():
    current = frontier.get()
    print(current)
    for nxt in neighbors(current):
        if nxt not in visited:
            frontier.put(nxt)
            nxt.frm = current
            visited.append(nxt)

spots = 0
for temp in visited:
    step = 0
    while temp.frm != None:
        temp = temp.frm
        step += 1
        if step > 50:
            break
    else:
        spots += 1   
print(spots)
for tile in visited:
    maze[tile.y][tile.x] = 'O'
printMaze()


    
