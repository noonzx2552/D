import random
data = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
sum = []
sum0 = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
for i in range(4):
    for j in range(5):
        num = random.randrange(0,1000)
        data[i][j] = num
for i in data:
    print(i)
for i in range(4):
    sum0 += int(data[i][0])
    sum1 += int(data[i][1])
    sum2 += int(data[i][2])
    sum3 += int(data[i][3])
    sum4 += int(data[i][4])

sum.insert(0,sum0)
sum.insert(1,sum1)
sum.insert(2,sum2)
sum.insert(3,sum3)
sum.insert(4,sum4)
print(f"total_sum: {sum}")