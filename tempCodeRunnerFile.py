import random
data = []
num = []
low = 0
high = 0
for i in range(10):
    r = random.randrange(0,100)
    data.append(r)
    num.append(r)

for i in range(0,10):
    if low > data[i]:
        low = data[i]
    else:
        low = low
print(low)