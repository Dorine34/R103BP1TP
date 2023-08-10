""" 
 Définition: Programme qui demande à l'utilisateur son nom et affiche ce nom sur le terminal.
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 3/08/2023    Version: 1.0 
"""

#affichage sur le terminal
print("quel est ton âge ?")
#saisir une valeur au clavier avec input et affectation de la variable age
age = int(input())

# affichage du contenu de la variable nom
print("Bonjour humain âgé de ", age, "ans.")

# test de la valeur de la variable age
if age < 18:
    print("Tu es mineur")
else:  
    print("Tu es majeur")

