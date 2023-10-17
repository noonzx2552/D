import random
daddy=[]
mom = []
kid = []
total_daddy = 0
total_mom = 0
total_kid = 0
for i in range(1,201):
    a = random.choice("SML")
    print(f"{i}.{a}")
    if a == "S":
        kid.append(f"{i}.{a}")
        total_kid += 1
    elif a == "M":
        mom.append(f"{i}.{a}")
        total_mom += 1
    else:
        daddy.append(f"{i}.{a}")
        total_daddy += 1
print(f"daddy:{daddy}")
print(f"-------------------------------------{total_daddy}-------------------------------------")
print(f"mom: {mom}")
print(f"-------------------------------------{total_mom}-------------------------------------")
print(f"kids: {kid}")
print(f"-------------------------------------{total_kid}-------------------------------------")