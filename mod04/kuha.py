kuha = int(input("Mikä on kuhan pituus senttimetreinä? "))
if kuha < 37:
    puuttuu = 37 - kuha 
    print("Kuha on alimittainen",puuttuu,"senttimetrillä.")
else:
    print("Hyvä saalis! Voit pitää sen.")
