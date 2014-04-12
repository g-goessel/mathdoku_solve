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
        return [(val_tot,)]
    
    combi=list()
    list_div=[i for i in range(1,10) if val_tot/i==int(val_tot/i)]
    combi_max=list(product(list_div, repeat=nbr_cases))

    if val_tot <= 9*nbr_cases:
        #on peut avoir une addition
        for i in list(product([i for i in range(1,10)],repeat=nbr_cases)):
            soustraction = reduce(lambda x,y: x-y, i)
            somme = sum(i)
            if somme == val_tot:
                combi.append(i)
            if soustraction == val_tot:
                combi.append(i)

    for i in combi_max:
        produit = reduce(lambda x,y: x*y, i)
        division = reduce(lambda x,y: x/y, i)
        if produit == val_tot:
            combi.append(i)
        if division == val_tot:
            combi.append(i)

    return combi

def bonoupas(matrice):
    """
    Cette foncton va tester si matrice est correcte ou pas en vérifiant que
    les chiffres n'apparaissent qu'une seule fois par ligne et par colonne

    Retourne True si matrice est valable et False dans le cas contraire

    """
    #on fixe (i_ref,j_ref) les coordonées d'une case que l'on veut vérifier comme étant unique sur ca ligne/colonne
    for i_ref in range(len(matrice)):
        for j_ref in range(len(matrice)):
            #On vérifie l'unicité sur la colonne
            for i in range(len(matrice)):
                if matrice[i][j_ref]==matrice[i_ref][j_ref] and i != i_ref: return False

            #Puis sur la ligne
            for j in range(len(matrice)):
                if matrice[i_ref][j]==matrice[i_ref][j_ref] and j != j_ref: return False


    return True
    

# Optimisations diverses

def optimize(user_data):
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
                        if user_data[bloc_to_clean][2][i][case_to_clean] == user_data[bloc_solo][0]: del(user_data[bloc_to_clean][2][i])


    return user_data