"""
fonctions 
"""

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


def combi_possible(val_tot,nbr_cases):
    """
    retourne la liste des combinaisons possibles
    """
    #test si la valeur est certaine
    if nbr_cases==1:
        return [val_tot]
    
    val_possibles=[]

    #test si addition possible
    if val_tot<=9*nbr_cases:
        for i in nbr_cases:
