def listefruits():
    fruits = ['pomme', 'cerise', 'orange']
    fruits.append('melon')
    return fruits

fruits = listefruits()

print(', ' .join(fruits))