luvut = []
leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))
luvut.append(luoti)
luvut.append(naula)
luvut.append(leiviska)
luotienmassa = luoti * 13.3
naulojenmassa = 13.3 * naula * 32
leiviskojenmassa = leiviska * 425.6 * 20
kokonaismassa = leiviskojenmassa + naulojenmassa + luotienmassa
kilot = int(kokonaismassa)
kg = int(kilot / 1000)
g = kokonaismassa % 1000
print("Massa nykymittojen mukaan: ",kg, "kg ja", g, "g")
