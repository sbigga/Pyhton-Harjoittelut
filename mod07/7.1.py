import random

def heitä_noppaa():
    silmäluku = random.randint(1, 6)
    return silmäluku

silmäluku = heitä_noppaa()
while silmäluku != 6:
    print(silmäluku)
    silmäluku = heitä_noppaa()

print(silmäluku)




