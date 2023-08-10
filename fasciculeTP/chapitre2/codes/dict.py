#affectation d'un dictionnaire
thisdict = {
  "nom": "Tabary",
  "profession": {"Enseignant", "chercheur", "Directice d'études", "Maitre de conférences"},
  "age": 1988
}

#affichage du dictionnaire
print("le disctionnaire est ",thisdict)

#affichage du dictonnaire clé par clé
for key in thisdict:
    print(key, "(cle) : ", thisdict[key], "(valeur)")

#vérification de l'existence d'une clé
if "age" in thisdict:
    print("La clé 'age' existe pour thisdict")

#affichage du dictionnaire ordonné
print (sorted(thisdict))

