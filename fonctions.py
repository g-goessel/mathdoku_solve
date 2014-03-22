"""
fonctions 
"""

from itertools import product
from functools import reduce

def clean(x, y, val, to_clean):
    """
    Cette fonction va nettoyer le tableau "to_clean" des combinaisons impossibles
    sur les lignes et les colonnes a partir d'une valeur considérée comme certaine "val"
    située aux coordonnées (x,y)
    """
    for ligne in range(len(to_clean)):
        # nettoyage de la ligne
        if ligne != x:
            for i in range(9):
                if to_clean[ligne, y, i] == val:
                    to_clean[ligne, y, i] = 0

    for colonne in range(len(to_clean)):
        # nettoyage de la colonne
        if colonne != y:
            for i in range(9):
                if to_clean[x, colonne, i] == val:
                    to_clean[x, colonne, i] = 0


def combi_possibles(val_tot,nbr_cases):
    """
    retourne la liste des combinaisons possibles
    """
    #test si la valeur est certaine
    if nbr_cases==1:
        return {'a': [val_tot]}
    
    combi_a=list()
    combi_m=list()
    combi_d=list()
    combi_s=list()

    combi_max=list(product([i for i in range (1,10)], repeat=nbr_cases))

    for i in combi_max:
        somme = sum(i)
        produit = reduce(lambda x,y: x*y, i)
        division = reduce(lambda x,y: x/y, i)
        soustraction = reduce(lambda x,y: x-y, i)
        if somme == val_tot:
            combi_a.append(i)
        if produit == val_tot:
            combi_m.append(i)
        if division == val_tot:
            combi_d.append(i)
        if soustraction == val_tot:
            combi_s.append(i)

    return {'a': combi_a, 'm': combi_m, 'd': combi_d, 's': combi_s}

