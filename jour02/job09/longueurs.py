def longueurs(a, b, c):
  if a + b > c and a + c > b and b + c > a:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
      print("Le triangle est rectangle")
    elif a == b and b == c:
      print("Le triangle est équilatéral")
    elif a == b or a == c or b == c:
      print("Le triangle est isocèle")
    elif ((a == b or a == c or b ==c) and (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2)):
        print("Le triangle est rectangle et isocèle")
    else:
      print("Le triangle est quelconque")
  else:
    print("Erreur de longueurs")

longueurs(3, 3, 4)
longueurs(4, 6, 5)
longueurs(3, 3, 3)
longueurs(1, 2, 3)