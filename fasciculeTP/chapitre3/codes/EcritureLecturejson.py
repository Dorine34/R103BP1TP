""" 
 Définition: Programme qui crée un fichier json contenant les cours
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 7/08/2023    Version: 1.0 
"""

# import pandas pour lire et écrire dans un fichier json
import pandas as panda 

# definition d'un dictionnaire
mesCours = [{'Cours':'Bases de la programmation', 'heures': 20, 'Durée':'30jours'},
        {'Cours':'Bases de Données relationnelles', 'heures': 30, 'Durée':'40jours'}]

# création d'un dataframe à partir du dictionnaire
df = panda.DataFrame(mesCours)
# création d'un fichier json à partir du dataframe
df.to_json('mesCoursFormatJSON.json')
# affichage du dataframe sur le terminal
print(df)