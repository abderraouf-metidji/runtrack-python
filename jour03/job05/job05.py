def nombrepremier(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3

    if n % i == 0:
        return False
        
    i = i + 2

    return True

for n in range(1000):
    if nombrepremier(n):
        print(n)