# Interface MathDoku

from fonctions import *
from bruteforce import *
from numpy import array

donnees = {}
taille=int(input('Taille de la grille ? '))
n = int(input('Nombre de blocs dans la grille \n'))
grille=array([[0 for i in range(taille)] for j in range(taille)])
try:
    for i in range(1,n+1):
        print('Votre grille : \n', grille)
        valeur = int(input('Valeur du bloc ' +str(i) +'\n'))
        nombre_elements = int(input('Nombre d\'éléments du bloc \n'))
        #si il y a plus de 7 éléments dans le bloc il est trop gourmand en RAM de calculer les possibilités
        if nombre_elements > 8 :
            print('Bloc trop grand pour être solvable, désolé')
            assert()
        liste_node = []
        liste_generale = [valeur]
        x_y = input('Entrez les coordonnées sous la forme (x,y),(x,y),... ')
        x_y=x_y.split('),(')
        if len(x_y) != nombre_elements: 
            print('Trop ou peu d\'éléments rentrés')
            assert()

        to_add=[ (int(x.replace('(','')),int(y.replace(')','')) ) for (x,y) in [i.split(',') for i in x_y] ]
        #on complete la grille de présentation
        for (x,y) in [i for i in to_add] :
            grille[x,y]=valeur

        liste_generale.append(to_add)
        #on rajoute les combinaisons possibles dans le dict
        liste_generale.append(combi_possibles(valeur,nombre_elements))
        donnees[i] = liste_generale

    print('Votre grille est : \n', grille)
    print(donnees)
    #l'utilisation d'une liste de listes est plus efficace qu'une matrice
    resultat=bruteforce(donnees.tolist(),taille)
    print('Résultat obtenu en ',resultat[1],'essais et ',resultat[2],'secondes :\n',array(resultat[0]))

except: 
    print('Une erreur s\'est produite, veuillez réessayer')



