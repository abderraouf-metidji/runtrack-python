string = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(string)):
  for j in range (0, i+1) :
    print(string[j], end="")
  print()