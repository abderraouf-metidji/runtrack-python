def printnombre(str):
    i = 0
    while (i < len(str)):
        i = i + 1
        if i == 26 or i == 37 or i == 88:
            continue
        print(i)

printnombre(range(0, 100))