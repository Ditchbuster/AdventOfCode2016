import hashlib

key = 'ugkcyxxp'
m = hashlib.md5()
m.update(key.encode())
out = m.digest()
flag = True
i = 0
password = []
while flag:
    check = key + str(i)
    m = hashlib.md5(check.encode())
    code = m.hexdigest()
    #print(code[:5])
    if code[:5] == '00000':
        password.append(code[5])
        if(len(password)>=8):
            break
    if i > 100000000:#code[:4]== '00000'
        break
    i += 1
print(password)
