#algo exo10
#variables

liste = list(range(1,101))
blacklist =[0]
check = True
number_use = 0             
#traitement
print(liste)
for x in liste:
    for i in blacklist:
             if x == i:
                 check = False
    if check:
             blacklist.append(x)
    else:
        number_use += 1
print("Il y a eu " + str(number_use) + " mot(s) déjà utilisé")


#fin
