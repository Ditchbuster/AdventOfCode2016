f = open("input.txt")


class Bot:

    def __init__(self, ident, low=None, high=None):
        self.ident = ident
        self.low = low
        self.lowO = False
        self.high = high
        self.highO = False
        self.values = []

    def give(self,value):
        if len(self.values) > 1:
            print("ERROR: bot %s is full".format(self.ident))
        self.values.append(value)
        self.values = sorted(self.values)
        #print(self.ident,self.values)

    def run(self, bots, output):
        if len(self.values) == 2:
            if self.values == [17,61]:
                print(self.ident)
            if self.high != None:
                if self.highO:
                    output[self.high] = self.values[1]
                else:
                    bots[self.high].give(self.values[1])
            if self.low != None:
                if self.lowO:
                    output[self.low] = self.values[0]
                else:
                    bots[self.low].give(self.values[0])
            self.values = []
            return True
        else:
            return False
                

bots = {}
output = {}
for line in f:
    parts = line.split()
    if parts[0] == 'bot':
        if parts[1] not in bots:
            bots[parts[1]] = Bot(parts[1])
        if parts[5] != "bot":
            bots[parts[1]].lowO = True
        bots[parts[1]].low = parts[6]
            
        if parts[10] != "bot":
            bots[parts[1]].highO = True    
        bots[parts[1]].high = parts[11]
    elif parts[0] == 'value':
        if parts[5] not in bots:
            bots[parts[5]] = Bot(parts[5])
        bots[parts[5]].give(int(parts[1]))
    else:
        print("ERROR")
        break

go = True
while go:
    go = False
    run = []
    for key in bots:
        if len(bots[key].values)== 2:
            run.append(key)
            go = True
    for key in run:
        bots[key].run(bots,output)
        print("RUNNING: " + key)
    for key in bots:
        if(bots[key].values != []):
            print (bots[key].ident, bots[key].values, bots[key].low, bots[key].high)
    print("######################")
print(output['0'],output['1'],output['2'])
