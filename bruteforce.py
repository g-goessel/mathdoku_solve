# Fichier contenant le bruteforce

from fonctions import *
from time import time
import numpy as np

def bruteforce(user_data,size):
    '''
    Cette fonction va résoudre la grille en utilisant une technique de bruteforce
    On va itérer par ordre croissant de possibilités
    '''
    t_start=time()

    #compteur global du nombre d'itération
    nbr_ite=0

    #classement des blocs bar ordre décroissant de combinaisons possibles
    sorted_blocs=sorted(user_data, key=lambda x : len(user_data[x][2]))
    print(sorted_blocs)

    #compteur des itérations de la forme {1:[ite en cours, nbr max d'ite], 2: ...}
    compteur=[[0,len(user_data[i][2])-1] for x,i in enumerate(sorted_blocs)]
    #la variable scope va faire référence à la position du bloc dans le compteur où nous sommes actuellement
    scope=0

    nbr_blocs=len(user_data)

    to_test = np.zeros((size,size),int)

    while 1:
        bloc_de_test=user_data[sorted_blocs[scope]]

        test=test_ajout(bloc_de_test[1], bloc_de_test[2][compteur[scope][0]],to_test, size)

        if test and scope==nbr_blocs-1:
            t_end=time()
            return True,to_test,nbr_ite,t_end-t_start
        elif test:
            #on a trouvé une combinaison convenable, on passe au bloc suivant
            scope+=1
        else:
            #on passe a la combinaison suivante
            while 1:
                if compteur[scope][0] == compteur[scope][1]:
                    nettoyage_matrice(to_test,user_data[sorted_blocs[scope]][1])
                    compteur[scope][0] = 0
                    if scope >0 :
                        scope -= 1
                    else :
                        return (False,'Pas de solution touvée')
                else:
                    compteur[scope][0] += 1
                    break
        nbr_ite+=1

        if not nbr_ite%50000:
            print(compteur)



def test_ajout(coordonnees,valeurs,matrice,size):
    """on test si le bloc peut rentrer dans la matrice"""

    #on rempli la matrice avec ce bloc
    for x,coord in enumerate(coordonnees):
        matrice[coord]=valeurs[x]
    #on test si il n'y a pas de contradiction
    for x in range(size):
        for y in range(size):
            valeur=matrice[x,y]
            if valeur!=0:
                if valeur in [matrice[x,i] for i in range(size) if i!=y]:
                    nettoyage_matrice(matrice,coordonnees)
                    return False
                if valeur in [matrice[i,y] for i in range(size) if i!=x]:
                    nettoyage_matrice(matrice,coordonnees)
                    return False
    return True,matrice

def nettoyage_matrice(to_clean,coords):
    """
    Va nettoyer la matrice to_clean des coordonnées coords
    """
    for coord in coords:
        to_clean[coord]=0
