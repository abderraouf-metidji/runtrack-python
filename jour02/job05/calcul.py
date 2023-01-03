def calcul(num1, operator, num2):
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    return num1 / num2
  elif operator == '%':
    return num1 % num2
  else:
    return "Erreur"

print(calcul(2, '*', 5))
print(calcul(20, '/', 5))
print(calcul(1, '%', 10))
print(calcul(5, '-', 2))
print(calcul(0, 0, 0))