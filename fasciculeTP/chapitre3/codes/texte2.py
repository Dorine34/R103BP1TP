""" 
 Définition: Programme qui concatène les fichiers bilbo1.txt, bilbo2.txt et bilbo3.txt 7
            dans un nouveau fichier bilbo.txt
            et qui remplace hobbit par Periannath dans le fichier bilbo.txt
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 7/08/2023    Version: 1.0 
"""

# Concaténation de fichiers
# ouverture du fichier en lecture
bilbo1 = open("fichiersTexte/bilbo1.txt", "r")
bilbo2 = open("fichiersTexte/bilbo2.txt", "r")
bilbo3 = open("fichiersTexte/bilbo3.txt", "r")
bilbo = open("fichiersTexte/bilbo.txt", "w")

# Ecriture dans le fichier
bilbo.write(bilbo1.read()+bilbo2.read()+bilbo3.read())

# Fermeture des fichiers (important)
bilbo.close()
bilbo1.close()
bilbo2.close()
bilbo3.close()


# Vérification du fichier créé
bilbo = open("fichiersTexte/bilbo.txt", "r")
print("Le hobbit  : \n", bilbo.read())
bilbo.close()


# Remplacement de hobbit par Periannath
with open("fichiersTexte/bilbo.txt", "r") as bilbo, open("fichiersTexte/bilboE.txt", "w") as bilboE:
    for ligne in bilbo:
        bilboE.write(ligne.replace("hobbit", "Periannath")) 

# Vérification du fichier créé
bilboE = open("fichiersTexte/bilboE.txt", "r")
print("\n Version elfique du hobbit : \n", bilboE.read())
bilboE.close()


