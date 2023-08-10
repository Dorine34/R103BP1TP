""" 
 Définition: Programme qui demande à l'utilisateur son nom et affiche ce nom sur le terminal.
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 3/08/2023    Version: 1.0 
"""

#tableau de la classe
listeEtudiants = ["Alice", "Bob", "Charlie", "Diane", "Alice", "Alice", "Charlie", "Charlie"]

#affichage des étudiants présents
dup = {x for x in listeEtudiants if listeEtudiants.count(x) > 1}
print(dup) 
