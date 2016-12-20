f = open("input.txt")
commands = []
inst = 0
for line in f:
    parts = line.split()
    commands.append(parts)
reg = [0]*4
print(reg)
while inst < len(commands):
    cmd = commands[inst]
    if cmd[0] == 'cpy':
        try:
            x = int(cmd[1])
            reg[ord(cmd[2])-97] = x
        except ValueError:
            reg[ord(cmd[2])-97] = reg[ord(cmd[1])-97]
    if cmd[0] == 'inc':
        reg[ord(cmd[1])-97] += 1
    if cmd[0] == 'dec':
        reg[ord(cmd[1])-97] -= 1
    if cmd[0] == 'jnz':
        try:
            x = int(cmd[1])
        except ValueError:
            x = reg[ord(cmd[1])-97]
        if x != 0:
            try:
                y = int(cmd[2])
            except ValueError:
                y = reg[ord(cmd[2])-97]
            inst += y
            continue
        
    inst += 1
print(reg)
