import random

tahko = int(input("Kerro nopan suurin luku: "))

def heitä_noppaa(tahko):
    silmäluku = random.randint(1, tahko)
    return silmäluku

silmäluku = heitä_noppaa(tahko)
while silmäluku != tahko:
    print(silmäluku)
    silmäluku = heitä_noppaa(tahko)

print(silmäluku)