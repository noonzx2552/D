print("#----------a----------#")
a1 = input("a1 :")
a2 = input("a2 :")
a3 = input("a3 :")
print("#----------b----------#")
b1 = input("b1 :")
b2 = input("b2 :")
b3 = input("b3 :")
a = [
    [ 0 , 0, 0],
    [ 0 , 0, 0],
    [ 0 , 0, 0]
]   
b = [
    [ 0 , 0, 0],
    [ 0 , 0, 0],
    [ 0 , 0, 0]
]
c = [
    [ 0 , 0, 0],
    [ 0 , 0, 0],
    [ 0 , 0, 0]
]
for i in range(3):
    a[0][i] = a1[i]
    a[1][i] = a2[i]
    a[2][i] = a3[i]
for i in range(3):
    b[0][i] = b1[i]
    b[1][i] = b2[i]
    b[2][i] = b3[i]
for i in range(3):
    c[0][i] = int(a[0][i]) + int(b[0][i])
    c[1][i] = int(a[1][i]) + int(b[1][i])
    c[2][i] = int(a[2][i]) + int(b[2][i])
for i in c:
    print(i)