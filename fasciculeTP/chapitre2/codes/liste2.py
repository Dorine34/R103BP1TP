
""" 
 Définition: Programme qui demande à l'utilisateur son nom et affiche ce nom sur le terminal.
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 3/08/2023    Version: 1.0 
"""

import random

#affectation d'une liste
listeTout = ['chat', 1, 'chien',3, 21, 
    'tortue', 1, True, False, 
    5, 5.5, 'b' 
    ]
listeEntiers = []
listeChaine = []
listeBool = []
listeFloat = []
listeAutre = []

#affichage de la liste
print("la liste est :", \
    listeTout)

#affectedation de la longueur de la liste à la variable longueurListeTout
longueurListeTout = len(listeTout)

#boucle de parcours de la liste
for i in range(longueurListeTout):
    if  type(listeTout[i]) == int:
        print("c'est un entier")
        listeEntiers.append(listeTout[i])
    elif type(listeTout[i]) == str:
        print("c'est une chaine de caractère")
        listeChaine.append(listeTout[i])
    elif type(listeTout[i]) == bool:    
        print("c'est un booléen")
        listeBool.append(listeTout[i])
    elif type(listeTout[i]) == float:    
        print("c'est un float")
        listeFloat.append(listeTout[i])
    else:
        print("c'est autre chose")
        listeAutre.append(listeTout[i])

listeEntiersSorted = sorted(listeEntiers)
listeChaineReverse = listeChaine[::-1]


#affichage des nouvelles listes        
print("les nouvelles listes sont :", \
    listeEntiersSorted, listeBool, listeChaineReverse, listeFloat, listeAutre)

#affectation de la nouvelle liste
maNouvelleListe = listeEntiersSorted[-2:-1] + listeBool[-2:-1] + \
    listeChaineReverse[-2:-1] + listeFloat[-2:-1] + listeAutre[-2:-1]
#affichage de la nouvelle liste
print("ma nouvelle liste est :", \
    maNouvelleListe)

#affichage d'une valeur aléatoire de la nouvelle liste
print("la valeur aléatoire est :", random.choice(maNouvelleListe)) 