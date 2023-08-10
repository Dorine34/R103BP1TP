element = 5 
liste_triee =[1,2,3,4,5,6,7,8,9,10]
a = 0
b = len(liste_triee)-1
m = (a+b)//2
while a < b :
    if liste_triee[m] == element:
        print("reponse : ", m)
        break
    elif liste_triee[m] > element:
        b = m-1
    else :
        a = m+1
    m = (a+b)//2

