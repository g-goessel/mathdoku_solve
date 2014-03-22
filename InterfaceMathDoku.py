# Interface MathDoku

from fonctions import *

Matrice_base = []
donnees = {}
lettres = ["a", "b", "c" , "d" ,"e" ,"f", "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
n = int(input('Nombre de blocs dans le 9x9 \n'))

print('Vous avez choisi exactement'+ str(n) +' blocs \n')
try:
    for i in range(1,n+1):
        lettre = lettres[i-1]
        valeur = int(input('Valeur du bloc ' +str(i) +'\n'))
        nombre_elements = int(input('Nombre d\'éléments du bloc \n'))
        #si il y a plus de 7 éléments dans le bloc il est trop gourmand en RAM de calculer les possibilités
        if nombre_elements > 8 :
            assert()
        liste_node = []
        liste_generale = [valeur]
        for vec in range(0, nombre_elements):
            node1 = int(input('Entrez x'+str(vec+1)))
            node2 = int(input('Entrez y'+str(vec+1)))
            node = (node1,node2)
            liste_node.append(node)
        liste_generale.append(liste_node)
        #on rajoute les combinaisons possibles dans le dict
        liste_node.append(combi_possibles(valeur,nombre_elements))
        donnees[lettre] = liste_generale

except: 
    print('Bloc trop grand pour être solvable, désolé')