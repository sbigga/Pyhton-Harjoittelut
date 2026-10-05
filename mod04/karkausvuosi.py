vuosiluku = int(input("Ilmoita vuosiluku: "))
if vuosiluku % 400 == 0:
    print("Kyseinen vuosi on karkausvuosi.")
elif vuosiluku % 100 == 0:
    print("Kyseinen vuosi ei ole karkausvuosi.")
elif vuosiluku % 4 == 0:
    print("Kyseinen vuosi on kaurkausvuosi.")
else:
    print("Kyseinen vuosi ei ole karkausvuosi.")