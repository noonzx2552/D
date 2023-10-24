#A = 65
words = input("word : ")
words=words.upper()
data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in words:
    c = ord(i)
    q = c-65
    data[q] += 1
    print(data)