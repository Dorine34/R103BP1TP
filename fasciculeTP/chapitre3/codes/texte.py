""" 
 Définition: Programme qui lit un texte et affiche les lignes qui contiennent un point.
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 7/08/2023    Version: 1.0 
"""

# ouverture du fichier en lecture
fichier = open("bilbo1.txt", "r")
print(fichier)

# lecture du fichier ligne par ligne
i = 0
for ligne in fichier:
    print("Ligne ", i, " :", ligne)
    i = i + 1
    # recherche du caractère point dans la ligne
    if ("." in ligne):
        print("Il y a un point dans la ligne ", i, " a la place ", ligne.find("."))
# fermeture du fichier
fichier.close()
