phone = input("type : ")
data = [0,0,0,0,0,0,0,0,0,0]
#----------------------------------#
for m in phone:
    m = int(m)
    data[m] += 1
print(data)
for n in range(0,len(data)):
    print(f"{n} = {data[n]}",end="")