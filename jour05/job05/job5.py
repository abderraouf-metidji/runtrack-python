def distanceparcourue(nb, h):
    distance_aller = nb * h
    distance_retour = distance_aller
    distance_jour = (distance_aller + distance_retour) * 5
    distance_semaine = distance_jour * 7
    distance_en_m = distance_semaine / 100
    return("Pour {} marches de {} cm, il parcourt {:.2f} m par semaine !"
        .format(nb, h, distance_en_m))

print(distanceparcourue(25,5))