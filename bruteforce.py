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
    sorted_blocs=sorted(user_data, key=lambda x : len(user_data[x][2]),reverse=True)

    #compteur des itérations de la forme {1:[ite en cours, nbr max d'ite], 2: ...}
    compteur=[[0,len(user_data[i][2])-1] for x,i in enumerate(sorted_blocs)]
    #la variable scope va faire référence à la position du bloc dans le compteur où nous sommes actuellement
    scope=0

    nbr_blocs=len(user_data)

    to_test = np.zeros((size,size))

    while 1:
        bloc_de_test=user_data[sorted_blocs[scope]]
        #print(bloc_de_test)
        test=test_ajout(bloc_de_test[1],bloc_de_test[2][compteur[scope][0]],np.copy(to_test),size)
        #print(test)

        if test and scope==nbr_blocs-1:
            return True,test[1]
            break
        elif test:
            scope+=1
            to_test=test[1]
        else:
            #on passe a la combinaison suivante
            while 1:
                if compteur[scope][0] == compteur[scope][1]:
                    compteur[scope][0] = 0
                    if scope >0 :
                        scope -= 1
                    else :
                        return (False,'Pas de solution touvée')
                else:
                    compteur[scope][0] += 1
                    break

            print(compteur,scope)
        nbr_ite+=1

        if not nbr_ite%10000:
            print(compteur)



def test_ajout(coordonnees,valeurs,matrice,size):
    """on test si le bloc peut rentrer dans la matrice"""

    #on rempli la matrice avec ce bloc
    for x,coord in enumerate(coordonnees):
        matrice[coord]=valeurs[x]
        #on test si il n'y a pas de contradiction
        for i in range(size):
            if matrice[coord[0],i] == valeurs[x] and i!=coord[1]: return False
            if matrice[i,coord[1]] == valeurs[x] and i!=coord[0]: return False
    return True,matrice
