import hashlib

key = 'ugkcyxxp'
#key = 'abc'
m = hashlib.md5()
m.update(key.encode())
out = m.digest()
flag = True
i = 0
passCount = 0
password = ['']*8
while flag:
    check = key + str(i)
    m = hashlib.md5(check.encode())
    code = m.hexdigest()
    #print(code[:5])
    if code[:5] == '00000' and not code[5].isalpha():
        index = int(code[5])
        if index<8 and password[index] == '':
            password[index]=code[6]
            passCount +=1
        if(passCount>=8):
            break
    if i > 100000000:#code[:4]== '00000'
        break
    i += 1
print(password)
