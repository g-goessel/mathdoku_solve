# Interface MathDoku

Matrice_base = []
donnees = {}
lettres = ["a", "b", "c" , "d" ,"e" ,"f", "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
n = int(input('Nombre de blocs dans le 9x9 \n'))

print('Vous avez choisi exactement'+ str(n) +' blocs \n')

for i in range(1,n+1):
    lettre = lettres[i-1]
    valeur = int(input('Valeur du bloc ' +str(i) +'\n'))
    nombre_elements = int(input('Nombre d\'éléments du bloc \n'))
    liste_node = []
    liste_generale = [valeur]
    for vec in range(0, nombre_elements):
        node1 = int(input('Entrez x'+str(vec+1)))
        node2 = int(input('Entrez y'+str(vec+1)))
        node = (node1,node2)
        liste_node.append(node)
    liste_generale.append(liste_node)
    donnees[lettre] = liste_generale
print(donnees)
