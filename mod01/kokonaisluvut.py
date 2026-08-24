import math
luvut = []
for i in range(3): 
    kokonaisluku = int(input("Anna kokonaisluku: "))
    luvut.append(kokonaisluku)
summa = sum(luvut)
print("Kokonaislukujen summa on: ", summa)
tulo = math.prod(luvut)
print("Kokonaislukujen tulo on: ", tulo)
keskiarvo = summa / 3
print("Kokonaislukujen keskiarvo on: ", keskiarvo)