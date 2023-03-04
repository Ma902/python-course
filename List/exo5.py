#algo anlayse de nombre pair et impair dans une liste

#variable
t1 = list(range(0,10))
pair = []
impair = []

#traitement
for x in t1:
    if x%2 == 0:
        pair.append(x)
    else:
        impair.append(x)

print("pair : "+str(pair))
print("impair : "+str(impair))
#fin