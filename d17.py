import random

A = []
B = []
C = []
total = 0

for i in range(100):
    lr = random.choice("LR")
    color = random.choice("ABCDEFGH")
    if lr == "L":
        A.append(color)
    elif lr == "R":
        B.append(color)

print(f"A: {A}")
print(f"B: {B}")

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            A[i] = '.'
            B[j] = '.'
            total += 1

print(f"A: {A}")
print(f"B: {B}")
print(f"Match: {total}")

