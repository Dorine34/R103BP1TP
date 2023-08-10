
""" 
 Définition: Programme qui donne le type des éléments d'une liste.
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 3/08/2023    Version: 1.0 
"""

#affectation d'une liste
listeTout = ['chat', 1, 'chien',3, 21, 
    'tortue', 1, True, False, 
    5, 5.5, 'b' 
    ]

#affichage de la liste
print("la liste est :", \
    listeTout)

#affectedation de la longueur de la liste à la variable longueurListeTout
longueurListeTout = len(listeTout)

#boucle de parcours de la liste
for i in range(longueurListeTout):
    if  type(listeTout[i]) == int:
        print("c'est un entier")
    elif type(listeTout[i]) == str:
        print("c'est une chaine de caractère")
    elif type(listeTout[i]) == bool:    
        print("c'est un booléen")
    elif type(listeTout[i]) == float:    
        print("c'est un float")
    else:
        print("c'est autre chose")
