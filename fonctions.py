"""
fonctions 
"""

from itertools import *
from functools import reduce


def combi_possibles(val_tot,nbr_cases,nbr_max):
    """
    retourne la liste des combinaisons possibles
    """
    #test si la valeur est certaine
    if nbr_cases==1:
        return [(val_tot,)]
    
    combi=list()
    list_div=[i for i in range(1,nbr_max+1) if val_tot/i==int(val_tot/i)]
    combi_max=list(product([i for i in range(1,nbr_max+1)], repeat=nbr_cases))
    combi_max_multipli=list(product(list_div, repeat=nbr_cases))

    if val_tot <= nbr_max**2:
        #on peut avoir une addition
        for i in combi_max:
            soustraction = reduce(lambda x,y: x-y, i)
            somme = sum(i)
            division = reduce(lambda x,y: x/y, i)
            if somme == val_tot:
                combi.append(i)
            if soustraction == val_tot:
                for j in list(permutations(i)):
                    combi.append(j)
            if division == val_tot:
                for j in list(permutations(i)):
                    combi.append(j)

    for i in combi_max_multipli:
        produit = reduce(lambda x,y: x*y, i)
        if produit == val_tot:
            combi.append(i)

    return combi

def bonoupas(matrice):
    """
    Cette foncton va tester si matrice est correcte ou pas en vérifiant que
    les chiffres n'apparaissent qu'une seule fois par ligne et par colonne

    Retourne True si matrice est valable et False dans le cas contraire

    """
    size = len(matrice)
    #on fixe (i_ref,j_ref) les coordonées d'une case que l'on veut vérifier comme étant unique sur ca ligne/colonne
    for i_ref in range(size):
        for j_ref in range(size):
            #On vérifie l'unicité sur la colonne
            for i in range(size):
                if matrice[i][j_ref]==matrice[i_ref][j_ref] and i != i_ref: return False

            #Puis sur la ligne
            for j in range(size):
                if matrice[i_ref][j]==matrice[i_ref][j_ref] and j != j_ref: return False


    return True
    

# Optimisations diverses

def optimize(user_data):
    """
    On peut enlever les doublons
    """
    for i in user_data:
        user_data[i][2]=list(set(user_data[i][2]))

    """
    On utilise les blocs avec une seule probabilité pour éliminer un grand nombre de cas certainement impossibles
    """


    #on récupère la liste des blocs unitaires
    blocs_solo=list()
    for i in user_data:
        if len(user_data[i][2])==1:
            blocs_solo.append(i)

    for bloc_solo in blocs_solo:
        coord_bloc_solo=user_data[bloc_solo][1][0]
        for bloc_to_clean in user_data:
            if bloc_to_clean==bloc_solo: pass
            else :
                #on crée la liste contenant la liste des cases qui vont nous intéresser dans bloc_to_clean
                cases_to_clean=[i for i,x in enumerate(user_data[bloc_to_clean][1]) if x[0]==coord_bloc_solo[0] or x[1]==coord_bloc_solo[1]]
                for case_to_clean in cases_to_clean:
                    for i,coord in enumerate(user_data[bloc_to_clean][2]):
                        if user_data[bloc_to_clean][2][i][case_to_clean] == user_data[bloc_solo][0]: 
                            print('removed ',user_data[bloc_to_clean][2][i],'from ',bloc_to_clean)
                            del(user_data[bloc_to_clean][2][i])


    """
    On efface des combinaisons qui ne sont pas possibles car le meme chiffre apparait plusieurs fois sur la meme ligne/colonne
    """
    for bloc in user_data:
        #Dans chaque bloc on liste tous les emplacements qui ne peuvent cohexister
        emplacements=[]

        liste_x=[i[0] for i in user_data[bloc][1]]
        liste_x_small=list(set(liste_x))
        for x in liste_x_small:
            if liste_x.count(x)>1:
                emplacements.append([i for i,j in enumerate(liste_x) if j == x])

        liste_y=[i[1] for i in user_data[bloc][1]]
        liste_y_small=list(set(liste_y))
        for y in liste_y_small:
            if liste_y.count(y)>1:
                emplacements.append([i for i,j in enumerate(liste_y) if j == y])

        #Ensuite on élimine les combinaisons qui ne respectent pas ce critère
        for key,combinaison in enumerate(user_data[bloc][2]):
            for combinaison_limitante in emplacements:
                coord_interessantes=[combinaison[i] for i in list(combinaison_limitante)]
                if len(coord_interessantes)!=len(set(coord_interessantes)):
                    print('poped ',user_data[bloc][2].pop(key))


    return user_data
