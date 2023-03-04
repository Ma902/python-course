#algo analyse de nombre de caractères
#variables
t1 =  ["Jean", "Maximilien", "Brigitte", "Sonia", "Jean-Pierre","Sandra"]
t2 = []     # moins de 6 caractères
t3 = []     # 6 caratères ou plus
#traitement
for x in t1:
    if len(x) < 6:
        t2.append(x)
    else:
        t3.append(x)

print("moins de 6 caractères : " + str(t2))
print("6 caractères ou plus : " + str(t3))

#fin