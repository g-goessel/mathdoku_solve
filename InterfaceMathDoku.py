# Interface MathDoku

from fonctions import *
from numpy import array


donnees = {}
lettres = ["a", "b", "c" , "d" ,"e" ,"f", "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
taille=int(input('Taille de la grille ? '))
n = int(input('Nombre de blocs dans la grille \n'))
grille=array([[0 for i in range(taille)] for j in range(taille)])
try:
    for i in range(1,n+1):
        print('Votre grille : \n', grille)
        lettre = lettres[i-1]
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
        donnees[lettre] = liste_generale

except: 
    print('Une erreur s\'est produite, veuillez réessayer')

""" resolution - bruteforce """ 
""" definir une matrice 9x9 """ 
matrice = array()
combinaisons = recupdico(donnees)
""" [ [combi1 bloc A], [combi2 bloc B],..........,......]"""   
resolu = False
i = 1
while resolu == False:
    for simultaneite in range(1,i):
        for n in range(1,len(combinaisons)):
            for k in range(1,len(combinaisons[n])):
                for elements in combinaisons[n][k]:
                    matrice = ['a remplir']
                    if cbonoupa(matrice) == True:
                        print('Résolu')
                        print(matrice)
                        resolu = True
                        break
        print(matrice)
    i+=1
        


print(grille)
