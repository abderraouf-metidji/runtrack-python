def fruitlegume(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("orange, mandarine et kiwi")
        elif saison == "ete":
            print("poire, fraise, cassis")
    elif type == "legume":
        if saison == "hiver":
            print("carotte, topinambour, endive")
        elif saison == "ete":
            print("artichaut, aubergine, navet")

fruitlegume("fruits", "hiver")
fruitlegume("fruits", "ete")
fruitlegume("legume", "ete")
fruitlegume("legume", "hiver")