import random
luku = int(input("Kerro arpakuutioiden lukumäärä: "))
summa = 0
for i in range(luku):
    heitto = random.randint(1,6)
    summa += heitto

print("Arpakuutioiden summa on:",summa)