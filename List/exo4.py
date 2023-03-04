#algo calcul liste
#vairabe
N = input("Combien de nombre pour votre liste ?")
t1 = []

#traitmement
if N.isdecimal():
    N = int(N)
    for x in range(N):
        t1.append(x)


    #question a

    counter = 0
    for x in t1:
        if x % 2 == 0:
            pass
        else:
            counter += 1
    
    print("il y a " + str(counter) + " Nombre(s) non nuls")

    #question b
    maximum = max(t1)
    print("le nombre le plus grand est : " + str(maximum))

    #question c
    minimum = min(t1)
    print("le nombre le plus petit est : " + str(minimum))

        #question d

    print("le nombre le plus petit et plus grand sont est : " + str(min(t1)) + " et " +str(max(t1)) )
else:
    print("veuillez choisir une valeur en décimal")

#fin

    
