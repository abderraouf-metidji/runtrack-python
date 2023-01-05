L = [8, 24, 48, 2, 16]

divisiblepar3 = 0

for i in L:
    if i % 3 == 0:
        divisiblepar3 = divisiblepar3 + 1

print(divisiblepar3)