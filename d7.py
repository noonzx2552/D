import random
data = []
num = []
for i in range(10):
    r = random.randrange(0,100)
    data.append(r)
    num.append(r)
for j in range(100):
    for k in range(0,10):
        ifelse = k+1
        if num[k] > num[ifelse]:
            num.insert(k+2,num[k])
            del num[k]
        else:
            num = num