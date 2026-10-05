luvut = []
luku = input("Kerro luku: ")

while luku != "":
    luvut.append(int(luku))
    luku = input("Kerro luku: ")
luvut.sort(reverse=True)
for luku in luvut[:5]:
    print(luku)
