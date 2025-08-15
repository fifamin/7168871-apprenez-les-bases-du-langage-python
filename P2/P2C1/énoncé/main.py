# Ecrivez votre code ici !
print("Donnez deux nombres")
nombre1 = input()
nombre2 = input()
#print(f"{nombre1}")
if nombre1.isnumeric() or nombre2.isnumeric():
   # print(nombre1)
    int(nombre1)
    int(nombre2)
    #print(nombre1)
    #print(nombre2)
else:
    raise SystemExit("Fin du programm")
print("Donnez le type d'operation +,-,*,/")

operation = input()
resultat = nombre1 + operation + nombre2

print(resultat)
