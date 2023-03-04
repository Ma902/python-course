#algo dernier jour du mois
#variables
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
t3 = []
#traitement
for x in range(len(t1)):
    t3.append(t2[x])    #ajoute la valeur du mois à t3
    t3.append(t1[x])    #ajoute le dernier jour du mois à  t3

print(t3)

#fin