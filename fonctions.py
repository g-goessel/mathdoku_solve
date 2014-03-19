"""
fonctions 
"""

<<<<<<< HEAD

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
=======
def clean(x, y ,val,to_clean):
	"""
	Cette fonction va nettoyer le tableau "to_clean" des combinaisons impossibles
	sur les lignes et les colonnes a partir d'une valeur considérée comme certaine "val"
	située aux coordonnées (x,y)
	"""
	for ligne in range(len(to_clean)):
		#nettoyage de la ligne
		if ligne!=x:
			for i in range(9):
				if to_clean[ligne,y,i]==val: 
					to_clean[ligne,y,i]=0

	for colonne in range(len(to_clean)):
		#nettoyage de la colonne
		if colonne!=y:
			for i in range(9):
				if to_clean[x,colonne,i]==val:
					to_clean[x,colonne,i]=0
>>>>>>> f8d83130e625a738400e44e659ea9f80562d4f85
