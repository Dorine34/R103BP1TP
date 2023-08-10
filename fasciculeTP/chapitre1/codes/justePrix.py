""" 
 Définition: Programme qui demande à l'utilisateur son nom et affiche ce nom sur le terminal.
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 3/08/2023    Version: 1.0 
"""

#importation de la librairie random
import random

#affectedation d'un nombre aléatoire entre 1 et 10 à la variable prix
prix = random.randint(1, 10)

#initialisation de la variable score
SCORE = 100

#initialisation de la variable tentatives
tentatives = 0


print("Devinez le juste prix ! Le prix est un nombre compris entre 1 et 10 inclus.")

#boucle de jeu
while True:
    nombre = int(input())
    tentatives += 1
    if nombre < prix:
        print("Le just prix est plus haut")
    if nombre > prix:
        print("Le juste prix est plus bas")
    if nombre == prix:
        print("Félicitations, vous avez trouvé le juste prix {} en {} essais, votre score est {} !".format(prix, tentatives, int(score / tentatives)))
        break

print("Partie terminée")