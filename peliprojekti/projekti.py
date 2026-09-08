esineet = []

def aloita_peli():
    print("Peliä ei ole vielä tehty valmiiksi, mutta voit aloittaa pelin myöhemmin.")

def lopeta_peli():
    print("Peli lopetetaan.")

def säännöt():
    print("Näytetään säännöt...")
    print("1. Älä huijaa.")
    print("2. Seuraa sääntöä 1")

def pelaajan_tiedot():
    print(f"Pelaajan nimi: {nimi}")
    print(f"Pelaajan ikä: {ikä}")

def lisää_esine():
    esine = input("Minkä esineen haluat lisätä? ")
    esineet.append(esine)
    print(f"Esine '{esine}' lisättiin esineisiin.")

def näytä_esineet():
    print("\nPelaajan esineet:")

    if len(esineet) == 0:
        print("Sinulla ei ole vielä esineitä.")
    else:
        for esine in esineet:
            print(f"- {esine}")

print("Anna pelaajan nimi:")
nimi = input()
print("Anna pelaajan ikä:")
ikä = input()
print(f"Pelaajan nimi: {nimi}")
print(f"Pelaajan ikä: {ikä}")

if int(ikä) < 12:
    print("Olet liian nuori pelaamaan peliä, peli sulkeutuu.")
else:
    print("Tervetuloa pelaamaan peliä!")

print("\nPäävalikko:")
print("1. aloita")
print("2. lopeta")
print("3. säännöt")
print("4. pelaajan tiedot")
print("5. lisää esine")
print("6. näytä esineet")
print("7. sammuta")

syöte = input("Valitse vaihtoehto (1-7): ")

while syöte != "7":

    if syöte == "1":
        aloita_peli()

    elif syöte == "2":
        lopeta_peli()

    elif syöte == "3":
        säännöt()

    elif syöte == "4":
        pelaajan_tiedot()

    elif syöte == "5":
        lisää_esine()

    elif syöte == "6":
        näytä_esineet()

    elif syöte =="7":
        print("peli sammutetaan")

    else:
        print("virheellinen valinta")

    print("\nPäävalikko:")
    print("1. aloita")
    print("2. lopeta")
    print("3. säännöt")
    print("4. pelaajan tiedot")
    print("5. lisää esine")
    print("6. näytä esineet")
    print("7. sammuta")
    syöte = input("Valitse vaihtoehto (1-7): ")