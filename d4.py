import random
sum = 0
data=[]
num = []
percenarray=[]
for i in range(101):
    a = random.randrange(0, 1000)
    data.append(a)
for j in range(101):
    sum += data[j]
print(f"sum: {sum}")
for x in range(0,100):
    percen = (data[x]/sum)*100
    percenarray.append(percen)
print(percenarray)
for y in range(0,100):
    if int(data[y]) % 3 == 0:
        num.append(data[y])
print(num)