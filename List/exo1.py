#Algo jour de la semaine
#variable

jour = ["lundi", "mardi", 2014, 21.4, "mercredi", "jeudi"]

suite = ["vendredi", "samedi", "dimanche"]

#traitement

del jour[2]     #value = 2014 
del jour[2]     #value = 21.4

for x in suite:
    jour.append(x)

print(jour)