import random
data0 = 0
data1 = 0
data2 = 0
data3 = 0 
data4 = 0
data5 = 0
data6 = 0
data7 = 0
dataL0 = 0
dataL1 = 0
dataL2 = 0
dataL3 = 0 
dataL4 = 0
dataL5 = 0
dataL6 = 0
dataL7 = 0
data = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
        ]
for i in range(8):
    for j in range(8):
        a = random.randrange(0,100)
        data[j][i] = a
for i in range(8):
    data0 += int(data[0][i])
    data[0][8] = data0
    data1 += int(data[1][i])
    data[1][8] = data1
    data2 += int(data[2][i])
    data[2][8] = data2
    data3 += int(data[3][i])
    data[3][8] = data3
    data4 += int(data[4][i])
    data[4][8] = data4
    data5 += int(data[5][i])
    data[5][8] = data5
    data6 += int(data[4][i])
    data[6][8] = data6
    data7 += int(data[5][i])
    data[7][8] = data7

for i in range(8):
    dataL0 += int(data[i][0])
    data[8][0] = dataL0
    dataL1 += int(data[i][1])
    data[8][1] = dataL1
    dataL2 += int(data[i][2])
    data[8][2] = dataL2
    dataL3 += int(data[i][3])
    data[8][3] = dataL3
    dataL4 += int(data[i][4])
    data[8][4] = dataL4
    dataL5 += int(data[i][5])
    data[8][5] = dataL5
    dataL6 += int(data[i][6])
    data[8][6] = dataL6
    dataL7 += int(data[i][7])
    data[8][7] = dataL7

for i in data:
    print(i)
