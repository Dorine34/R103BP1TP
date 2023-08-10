""" 
 Définition: Programme qui demande à l'utilisateur son nom et affiche ce nom sur le terminal.
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 3/08/2023    Version: 1.0 
"""

#tableau de la classe
listeEtudiants = ["Alice", "Bob", "Charlie", "Diane"]



#verification de la présence des étudiants
for w in listeEtudiants:
    print("L'étudiant ",w, "est-il venu en cours ?")
    reponse = input()
    #verification de la réponse
    while reponse != "y" and reponse != "n":
        print("reponse incorrecte, veuillez saisir y ou n")
        reponse = input()
    if reponse == "y":
        print("L'étudiant ",w, "est-il bien orthographié ?")
        reponse = input()
        #verification de la réponse
        while reponse != "y" and reponse != "n":
            print("reponse incorrecte, veuillez saisir y ou n")
            reponse = input()
        if reponse == "n":
            #modification de l'orthographe
            print("Veuillez ressaisir le nom de l'étudiant")
            nouveauNom = input()
            #verification de la réponse
            print("souhaitez-vous remplacer ", w, " par ", nouveauNom, " ?")
            reponseOrthographie = input()
            #boucle de vérification de la réponse
            while reponseOrthographie == "n":
                print("Veuillez ressaisir le nom de l'étudiant")
                nouveauNom = input()
                print("souhaitez-vous remplacer ", w, " par ", nouveauNom, " ?")
                reponseOrthographie = input()
                #remplacement de l'ancien nom par le nouveau dans la liste
                listeEtudiants = list(map(lambda x: x.replace(w, nouveauNom), listeEtudiants))

#affichage des étudiants présents
print(listeEtudiants)
