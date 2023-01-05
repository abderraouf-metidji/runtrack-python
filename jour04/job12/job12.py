def tri(liste):
    i = []
    while liste:
        mini=min(liste)
        liste.remove(mini)
        i.append(mini)
    return i

print(tri([55, 25, 15, 1, 5, 105, 22, 3]))