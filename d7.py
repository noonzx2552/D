import random
data = []
loca = []
low = 0
high = 0
for i in range(10):
    r = random.randrange(0,100)
    data.append(r)
    loca.append(r)

low = data[0]
high = data[0]
for num in data:
    if num < low:
            low = num 
    if num > high:
            high = num

posmin = loca.index(low)
maxpos = loca.index(high)
print(loca)
print(f"lowpaos:{posmin}")
print(f"highpos:{maxpos}")
print(f"low:{low}")
print(f"high:{high}")
print(f"data:{data}")