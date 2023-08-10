
""" 
 Définition: Programme qui demande à l'utilisateur son nom et affiche ce nom sur le terminal.
 réalisé dans le cadre du module R1.03 Bases de la programmation
 Auteur: Mme Tabary
 Date: 3/08/2023    Version: 1.0 
"""


#affectation d'une liste
listeTest = ['J\'étudie dans la formation du','BUT', 'Sciences', 'des', 'Données' ]

#création d'une chaine de caractère à partir d'une liste
monString = " ".join(listeTest)

print(monString)

#découpage de la chaine de caractère en liste
listeFinale = monString.split()

#affichage de la liste
print("la liste est :", listeFinale)

#affichez le nombre de mots de la liste
print("le nombre de mots de la liste est :", len(listeFinale))

#affichez le nombre d’occurrences du mot "BUT"
print("le nombre d’occurrences du mot \"BUT\" est :", listeFinale.count("BUT"))

#rajouter entre "J'étudie" et "dans" les éléments "à", "Dole"
listeFinale.insert(1, "à")
listeFinale.insert(2, "Dole")
print("la liste est :", listeFinale)

#supprimer le mot "Données"
listeFinale.remove("Données")

#supprimer le mot "des"
listeFinale.remove("des")

monStringFinal = " euh ".join(listeFinale)
print("le string devient :", monStringFinal)

#afficher le string en majuscule
monStringFinalMaj = monStringFinal.upper()
print("le string en majuscule est :", monStringFinalMaj)

#remplacez les mots "euh" par des espaces
monStringFinalMajSansEUH = monStringFinalMaj.replace("EUH", " ")

print("le string sans euh est :", monStringFinalMajSansEUH)

#vérifiez si le mot "Dole" est dans le string
print("le mot \"Dole\" est-il dans le string ? :", "DOLE" in monStringFinalMajSansEUH)

#affichez le string en minuscule
monStringFinalMajSansEUHlower = monStringFinalMajSansEUH.lower()
print("le string en minuscule est :", monStringFinalMajSansEUHlower)
print(monStringFinalMajSansEUHlower.split())
