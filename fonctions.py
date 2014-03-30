"""
fonctions 
"""

from itertools import product
from functools import reduce


def combi_possibles(val_tot,nbr_cases):
    """
    retourne la liste des combinaisons possibles
    """
    #test si la valeur est certaine
    if nbr_cases==1:
        return {'a': [val_tot]}
    
    combi=list()

    combi_max=list(product([i for i in range (1,10)], repeat=nbr_cases))

    for i in combi_max:
        somme = sum(i)
        produit = reduce(lambda x,y: x*y, i)
        division = reduce(lambda x,y: x/y, i)
        soustraction = reduce(lambda x,y: x-y, i)
        if somme == val_tot:
            combi.append(i)
        if produit == val_tot:
            combi.append(i)
        if division == val_tot:
            combi.append(i)
        if soustraction == val_tot:
            combi.append(i)

    return combi

def cbonoupa(matrice):
    """
    Cette foncton va tester si matrice est correcte ou pas en vérifiant que
    les chiffres n'apparaissent qu'une seule fois par ligne et par colonne

    Retourne True si matrice est valable et False dans le cas contraire

    Il suffit de verifier les cases de la "diagonale" de la matrice
    """
    for i in range(len(matrice)):
        nombre_a_test=matrice[i,i]
        for j in range(len(matrice)):
            if j != i and (matrice[i,j]==nombre_a_test or matrice[j,i]==nombre_a_test):
                return False

    return True
    