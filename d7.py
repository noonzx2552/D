import random
data = []
num = []
for i in range(10):
    r = random.randrange(0,100)
    data.append(r)
    num.append(r)
for j in range(100):
    for k in range(0,10):
        if num[k-1] < num[k]:
            num.insert(k+2,num[k])
            del num[k]
        else:
            num = num

for z in range(0,10):
    a = data[z]
    print(a)