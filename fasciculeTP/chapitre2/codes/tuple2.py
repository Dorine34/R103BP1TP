
""" 
 Définition: Programme qui demande à l'utilisateur son nom et affiche ce nom sur le terminal.
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


print("la somme des dépenses est de : ", sum(mesPrevisionsTroisMois))
print("la dépense la plus importante est de : ", max(mesPrevisionsTroisMois))
print("la dépense la moins importante est de : ", min(mesPrevisionsTroisMois))
print("le nombre de dépenses est de : ", len(mesPrevisionsTroisMois))
print("la moyenne des dépenses est de : ", sum(mesPrevisionsTroisMois)/len(mesPrevisionsTroisMois))
print("la somme des dépenses est de : ", sum(mesPrevisionsTroisMois))
print("le nombre de dépenses égales à 423 est de : ", mesPrevisionsTroisMois.count(423))
print("le nombre de dépenses supérieures à 100 est de : ", len([x for x in mesPrevisionsTroisMois if x > 100]))