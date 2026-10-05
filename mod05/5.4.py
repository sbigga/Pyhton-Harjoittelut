import random

luku = random.randint(1,10)
arvaus = 0

while arvaus != luku: 

    arvaus = int(input("Anna arvaus: "))

    if arvaus > luku:
        print("Liian suuri arvaus.")
    elif arvaus < luku: 
        print("Liian pieni arvaus.")

print("Oikein!")


