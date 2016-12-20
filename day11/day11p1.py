import copy
lvl = 0
startFloors = [[['th','c'],['pl','g'],['st','g'],['th','g']],[['pl','c'],['st','c']],
          [['pr','g'],['pr','c'],['ru','g'],['ru','c']],[]]
testFloors = [[['hd','c'],['li','c']],[['hd','g']],[['li','g']],[]]
startFloors = testFloors
solution = []
states = [[],[],[],[],[]] # colapsed states, movs to that state, done state, states id, previous state id
startElevator = 0
def printFloors(floors):
    for i in range(len(floors)):
        print("F"+str(i),floors[i])

def floorsValid(floors):
    for fl in floors:
        for i in range(len(fl)):
            if fl[i][1] == 'c':
                paired = False
                gen = False
                for el in fl:
                    if el[1] == 'g' and el[0] == fl[i][0]:
                        paired = True
                    elif el[1] == 'g':
                        gen = True
                if paired == False and gen == True:
                    return False
    return True

def colapse(floors,elevator):
    mashed = str(elevator) + '.'
    for fl in floors:
        flStr = []
        for el in fl:
            flStr.append(el[0]+el[1])
        flStr = sorted(flStr)
        for el in flStr:
            mashed += el
        mashed += '.'
    return mashed

def checkDone(floors):
    done = True
    for i in range(len(floors)):
        if len(floors[i]) != 0 and i != 3:
            done = False
    return done

def backMoveLen(stateInd, pnt = False):
    global states
    if pnt:
        print(states[3])
        print(states[4])
    moves = 0
    curId = states[3][stateInd]
    if pnt:
        print("Start: " + str(curId))
    while curId != 1:
        moves += 1
        ind = states[3].index(curId)
        curId = states[4][ind]
        if pnt:
            print(curId)
            print(states[1][ind][-1])
    return moves

def move(floors, elevator, moves, prevIdent):
    global lvl
    global states

    lvl += 1
    ident = lvl
    if len(moves)>0:
        print('#'+str(ident)+' '+str(prevIdent),moves[-1],len(moves))
    
    #printFloors(floors)
    if not floorsValid(floors):
        print("Not vaild")
        return (False,None)
    
    mashed = colapse(floors,elevator)
    if mashed in states[0]:
        ind = states[0].index(mashed)
        if backMoveLen(ind) <= len(moves):
            print(str(ident)+" in states as " + str(states[3][ind]))
            return (False,None)
        else:
            print(str(ident) + " in states but less then " +str(states[3][ind]))
            states[1][ind] = moves
            states[4][ind] = prevIdent
            return (False,None)
    #### Adding state ####
    states[0].append(mashed)
    states[1].append(moves)
    states[3].append(ident)
    states[4].append(prevIdent)
    if checkDone(floors):
        states[2].append(1)
        print("DONE!")
        return (True,moves)
    states[2].append(0)

    #### calc next moves ####
    vailds = []
    for el in floors[elevator]: # for each element on the floor with elevator, move it
        if elevator != 3: # move el up
            fls = copy.deepcopy(floors)
            elv = elevator
            mvs = copy.deepcopy(moves)
            mvs.append((el.copy(),None,'u'))
            fls[elv].remove(el)
            fls[elv+1].append(el)
            done = move(fls,elv+1,mvs,ident)
            if done[0]:
                vailds.append(done[1])
        if elevator != 0: # move el down
            fls = copy.deepcopy(floors)
            elv = elevator
            mvs = copy.deepcopy(moves)
            mvs.append((el.copy(),None,'d'))
            fls[elv].remove(el)
            fls[elv-1].append(el)
            done = move(fls,elv-1,mvs,ident)
            if done[0]:
                vailds.append(done[1])
        ##### move two at once ######
        if len(floors[elevator]) > 1:
            for el2 in floors[elevator]:
                if el2 == el:
                    continue
                if elevator != 3: # move el up
                    fls = copy.deepcopy(floors)
                    elv = elevator
                    mvs = copy.deepcopy(moves)
                    mvs.append((el.copy(),el2.copy(),'u'))
                    fls[elv].remove(el)
                    fls[elv].remove(el2)
                    fls[elv+1].append(el)
                    fls[elv+1].append(el2)
                    done = move(fls,elv+1,mvs,ident)
                    if done[0]:
                        vailds.append(done[1])
                if elevator != 0: # move el down
                    fls = copy.deepcopy(floors)
                    elv = elevator
                    mvs = copy.deepcopy(moves)
                    mvs.append((el.copy(),el2.copy(),'d'))
                    fls[elv].remove(el)
                    fls[elv].remove(el2)
                    fls[elv-1].append(el)
                    fls[elv-1].append(el2)
                    done = move(fls,elv-1,mvs,ident)
                    if done[0]:
                        vailds.append(done[1])
               

    if len(vailds) > 0:
        minLen = len(vailds[0])
        minMvs = vailds[0]
        for mvs in vailds:
            if len(mvs) < minLen:
                minLen = len(mvs)
                minMvs = mvs
        return (True,minMvs)
    else:
        return (False,None)

ret = move(startFloors,startElevator,[],lvl)
if ret[0]:
    for i in range(len(states[0])):
        if states[2][i] == 1:
            print(backMoveLen(states[3][i],True))
