import random
data = []
for i in range(10):
    r = random.randrange(0, 100)
    data.append(r)
print(data)
for i in range(10):
    for j in range(0, 9 - i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]  
print(data)