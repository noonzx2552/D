words = input("word : ")
data = []
a = len(words)
for i in words:
    data.append(i)
count = []
for i in data:
    if data[i] == count:
        count[i] += 1
    else:
        count[i] = 1

for i in count:
    print(i)