""" 
 Définition: Programme qui affiche la population des communes dont le nom commence par Dol
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 7/08/2023    Version: 1.0 
"""

# import de la bibliothèque pandas
import pandas as panda

# affectation des noms de colonnes qui nous intéressent
colonnes = ['nomCommune','population']

# lecture du fichier excel
df = panda.read_excel(open('fichiersXLSX/ensemble.xlsx', 'rb'), 
    sheet_name='Communes',  
    usecols=[6,9], 
    names = colonnes)

# affichage de la population des communes dont le nom commence par Dol
for idx, x in enumerate(df.nomCommune):
    if type(x) == str and x.startswith('Dol'):
        print("Population de", x, "égale ", df.population[idx])
    

