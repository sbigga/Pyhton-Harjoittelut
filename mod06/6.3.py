luku = int(input("Kerro kokonaisluku: "))

alkuluku = True

for jakaja in range(2, luku):
    if luku % jakaja == 0:
        alkuluku = False

if alkuluku:
    print("Kyseessä on alkuluku.")
else:
    print("Kyseessä ei ole alkuluku.")