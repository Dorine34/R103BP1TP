""" 
 Définition: Programme qui demande à l'utilisateur son nom et affiche ce nom sur le terminal.
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 2/08/2023    Version: 1.0 
"""

#affichage sur le terminal
print("Bonjour, quel est ton nom ?")
#saisir une valeur au clavier avec input et affectation de la variable nom
nom = input()

#affichage sur le terminal
print("quel est ton âge ?")
#saisir une valeur au clavier avec input et affectation de la variable age
age = input()

#affichage sur le terminal
print("quel est ta taille ?")
#saisir une valeur au clavier avec input et affectation de la variable taille
taille = input()


ANNEE = 2023
# affichage du contenu de la variable nom
print("Bonjour humain au nom de", nom, ", âgé de ", age, " ans, né en ", ANNEE - int(age),
 "et mesurant", taille[:1], "m", taille[1:3], "cm.")

