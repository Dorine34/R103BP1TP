
""" 
 Définition: Programme de manipulation de tuples.
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 3/08/2023    Version: 1.0 
"""

#affectation d'un tuple
depensesTuple = (5, 21, 101, 423)

#affectation de variables
(gaz, forfait, course, loyer) = depensesTuple

#affichage des variables
print ("le tuple est :")
print(course)
print(forfait)
print(loyer)

#affectation tuple sur 3 mois
mesPrevisionsTroisMois = depensesTuple * 3

#affichage du nouveau tuple
print(mesPrevisionsTroisMois)
