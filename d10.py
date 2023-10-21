import random
import math
password = []
inpu = int(input("type-lenpassword: "))
if inpu % 2 == 0:
    low = (inpu-2) / 2
    high = (inpu-2) / 2
else:
    f = random.choice("ab")
    if f == "a":
        low = (inpu-2) / 2
        low = math.ceil(low)
        high = (inpu-2) - low
    else:
        high = (inpu-2) / 2
        high = math.ceil(high)
        low = (inpu-2) - high
num = random.randrange(0, 10)
password.append(num)    
sanyarug = random.choice("@#$_")
password.append(sanyarug)
for i in range (int(high)):
    upper = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    loca = random.randrange(0,len(password))
    password.insert(loca,upper)
for i in range (int(low)):
    zzz = len(password)
    lower = random.choice("abcdefghijklmnopqrstuvwxyz")
    loca = random.randrange(0,len(password))
    password.insert(loca,lower)
for i in password:
    print(i, end='')