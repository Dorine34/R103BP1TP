
""" 
 Définition: Programme qui transforme une liste en une chaîne de caractère.
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 3/08/2023    Version: 1.0 
"""


#affectation d'une liste
listeTest = ['J\'étudie dans la formation du','BUT', 'Sciences', 'des', 'Données' ]

#création d'une chaine de caractère à partir d'une liste
monString = " ".join(listeTest)

print(monString)

#découpage de la chaine de caractère en liste
listeFinale = monString.split()

#affichage de la liste
print("la liste est :", listeFinale)