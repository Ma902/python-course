#algo exercice 9

#variables



#traitement

word = input("Choisir un mot : ")


liste = list(word)

liste.reverse()
word_reverse = ""
for x in liste:
    word_reverse += x
if word_reverse == word:
    print("Mot Palindrome")
else:
    print("Mot non Palindrome")


#fin
