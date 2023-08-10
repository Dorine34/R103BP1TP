""" 
 Définition: Programme qui compte le nombre de lignes dans un fichier csv
            et qui énumère les prénoms féminins des personnes nées en 2021, 
                dont le prénom a été donné 4 fois
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 7/08/2023    Version: 1.0 
"""

# import csv pour lire et écrire dans un fichier csv
import csv

# ouverture du fichier 
with open('fichiersCSV/Dpt39depuis2000.csv') as moncsv:
    # lecture du fichier csv
    csv_reader = csv.reader(moncsv, delimiter=',')
    # compteur de lignes
    line_count = 0
    for ligne in csv_reader:
        if line_count == 0:
            # affichage du nom des colonnes
            print(f'Les colonnes sont :  {", ".join(ligne)}')
        # incrémentation du compteur de lignes
        line_count += 1
        
        # affichage des prénoms féminins des personnes nées en 2021, dont le prénom a été donné 4 fois
        if ligne[0].split(";")[2] == "2021" and ligne[0].split(";")[0] == "2" and ligne[0].split(";")[4] == "4":
            print("Prénom : ", ligne[0].split(";")[1])
    # affichage du nombre de lignes total
    print(f'Au total, il y a {line_count} lignes.')
