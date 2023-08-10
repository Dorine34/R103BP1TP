

"Exemple de tuple avec une liste à l'intérieur
liste1 = [0, 1, 2]
tuple1 = (liste1, "Plouf")

print ("mon tuple =",tuple1)
#sortie écran : "mon tuple = ([0, 1, 2], 'Plouf')"


#Objectif : avoir "mon tuple = ([1, 1, 2], 'Plouf')"
# Mais on ne peut pas modifier un tuple :
# tuple1[0] = [1, 1,2] : ERREUR

#On peut modifier une liste :
liste1[0] = 1

print ("apres modification de l1, on a mon Tuple=",tuple1)
#sortie écran : "apres modification de l1, on a mon Tuple= ([1, 1, 2], 'Plouf')"

#Observation : on peut modifier la liste à l'intérieur du tuple


