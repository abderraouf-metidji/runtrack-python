def listefruits():
    fruits = ["pomme", "cerise", "orange", "melon"]
    fruits.insert(2, "mangue")
    return fruits

fruits = listefruits()

print(', ' .join(fruits))