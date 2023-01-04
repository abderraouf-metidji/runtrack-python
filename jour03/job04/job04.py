def printnombre(str):
    i = 0
    while (i < len(str)):
        i = i + 1
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

printnombre(range(0, 101))