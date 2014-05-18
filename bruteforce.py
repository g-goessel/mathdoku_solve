# Fichier contenant le bruteforce
from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED
from fonctions import *
from time import time

def bruteforce(user_data,size):
    '''
    Cette fonction va résoudre la grille en utilisant une technique de bruteforce
    On va itérer par ordre croissant de possibilités
    '''
    global t_start
    t_start=time()

    #classement des blocs bar ordre décroissant de combinaisons possibles
    sorted_blocs_reversed=sorted(user_data, key=lambda x : len(user_data[x][2]),reverse=True)
    sorted_blocs=sorted(user_data, key=lambda x : len(user_data[x][2]))

    #compteur des itérations de la forme {1:[ite en cours, nbr max d'ite], 2: ...}
    compteur=[[0,len(user_data[i][2])-1] for x,i in enumerate(sorted_blocs)]
    compteur_reversed=[[0,len(user_data[i][2])-1] for x,i in enumerate(sorted_blocs_reversed)]


    user_data_reversed={i:[user_data[i][0],user_data[i][1],list(reversed(user_data[i][2]))] for i in user_data}

    arg_list=[(user_data,sorted_blocs,compteur,size), (user_data,sorted_blocs,compteur,size)]

    with ProcessPoolExecutor() as executor:
        futures=[executor.submit(worker,user_data,sorted_blocs,compteur,size),executor.submit(worker,user_data_reversed,sorted_blocs,compteur,size)]
        results=wait(futures,return_when=FIRST_COMPLETED)
        retour=list(results.done)[0].result()
        return retour

def worker(user_data,sorted_blocs,compteur,size):
    print('worker started')
    #compteur global du nombre d'itération
    nbr_ite=0

    #la variable scope va faire référence à la position du bloc dans le compteur où nous sommes actuellement
    scope=0

    nbr_blocs=len(user_data)

    to_test = [[0 for i in range(size)] for j in range(size)]

    while 1:
        bloc_de_test=user_data[sorted_blocs[scope]]

        test=test_ajout(bloc_de_test[1], bloc_de_test[2][compteur[scope][0]],to_test, size)
        if test and scope==nbr_blocs-1:
            global t_start
            t_end=time()
            return True,test[1],nbr_ite,t_end-t_start
        elif test:
            #on a trouvé une combinaison convenable, on passe au bloc suivant
            to_test=test[1]
            scope+=1
        else:
            #on passe a la combinaison suivante
            while 1:
                if compteur[scope][0] == compteur[scope][1]:
                    to_test=nettoyage_matrice(to_test,user_data[sorted_blocs[scope]][1])
                    compteur[scope][0] = 0
                    if scope >0 :
                        scope -= 1
                    else :
                        return False,nbr_ite
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
        matrice[coord[1]][coord[0]]=valeurs[x]
    #on test si il n'y a pas de contradiction
    for x in range(size):
        for y in range(size):
            valeur=matrice[x][y]
            if valeur!=0:
                if valeur in [matrice[x][i] for i in range(size) if i!=y]:
                    nettoyage_matrice(matrice,coordonnees)
                    return False
                if valeur in [matrice[i][y] for i in range(size) if i!=x]:
                    nettoyage_matrice(matrice,coordonnees)
                    return False
    return True,matrice

def nettoyage_matrice(to_clean,coords):
    """
    Va nettoyer la matrice to_clean des coordonnées coords
    """
    for coord in coords:
        to_clean[coord[1]][coord[0]]=0

    return to_clean
