""" 
 Définition: Programme interactif de vérification de la présence d'étudiants.
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 3/08/2023    Version: 1.0 
"""

#tableau de la classe
listeEtudiants = ["Alice", "Bob", "Charlie", "Diane"]
listeEtudiantsAbs = []

#verification de la présence des étudiants
for w in listeEtudiants:
    print("L'étudiant ",w, "est-il venu en cours ?")
    reponse = input()
    #verification de la réponse
    while reponse != "y" and reponse != "n":
        print("reponse incorrecte, veuillez saisir y ou n")
        reponse = input()
    if reponse == "n":
        listeEtudiantsAbs.append(w)

#affichage des étudiants présents
for w in listeEtudiantsAbs:
    print("Nom de l'étudiant absent : ",w)
    for     x in listeEtudiantsAbs:
        print("Nom de l'étudiant absent : ",w)