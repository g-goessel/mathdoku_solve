# Fichier contenant le bruteforce

#from numpy import array
from fonctions import *
from time import time

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
    compteur={ i:[0,len(user_data[i][2])-1] for i in user_data}
    gen_grille=[[0 for i in range(size)] for j in range(size)]

    while 1:
        #on passe aux choses sérieuses : le remplissage de la grille to_test
        to_test=list(gen_grille)

        for bloc in user_data:
            i=0
            for case in user_data[bloc][1]:
                to_test[case[0]-1][case[1]-1]=user_data[bloc][2][compteur[bloc][0]][i]
                i+=1

        #on test si cette grille est correcte
        if  bonoupas(to_test)==True:
            t_end=time()
            return to_test,nbr_ite,t_end-t_start
            break
        else : 
            #sinon on passe à la combinaison suivante
            i=0
            while 1:
                try:
                    if compteur[sorted_blocs[i]][0]+1 < compteur[sorted_blocs[i]][1]:
                        compteur[sorted_blocs[i]][0]+=1
                        #debugage : on print le compteur toutes les 10^5 itérations
                        if nbr_ite/(10**5)==nbr_ite//(10**5):
                            print([compteur[i] for i in sorted_blocs])
                        break
                    else:
                        compteur[sorted_blocs[i]][0]=0
                        i+=1
                except :
                    return (False,'Pas de solution touvée')
        nbr_ite+=1
