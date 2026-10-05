import random

TIEDOSTO = "tallennus.txt"
VALIKKO = ("Aloita peli", "Ohjeet", "Löydetyt pakotiet", "Lopeta")  

LOPUT = {
    "vartija": ("Naamioidu vartijaksi",
                "Jeffrey kävelee pääportista ulos vartijan univormussa. VAPAA!"),
    "kierratys": ("Kierrätysauton kyydissä",
                  "Auto jättää Jeffreyn kaatopaikan sijaan kierrätyskeskukseen. VAPAA!"),
    "taivas": ("Pako taivaaseen",
               "Jeffrey leijuu pilvien yläpuolelle ja vilkuttaa vankilalle. VAPAA!"),
}


# ---------- Luokat ----------

class Hahmo:
   

    def __init__(self, nimi):  
        self.nimi = nimi

    def puhu(self, teksti):
        print(f"{self.nimi}: {teksti}")


class Pelaaja(Hahmo): 


    def __init__(self, nimi):
        super().__init__(nimi)
        self.energia = 10
        self.esineet = []  

    def nayta_reppu(self):
        if not self.esineet:
            print("Reppu on tyhjä.")
        for esine in self.esineet:
            print(f" - {esine}")


class Vartija(Hahmo):  
    
    def __init__(self, nimi, tarkkaavaisuus):
        super().__init__(nimi)
        self.tarkkaavaisuus = tarkkaavaisuus  

    def huomaako(self, naamioitu):
        raja = self.tarkkaavaisuus - (4 if naamioitu else 0)
        return random.randint(1, 10) <= raja


# ---------- Tiedostonkäsittely ----------

def tallenna_loppu(tunnus):
    with open(TIEDOSTO, "a", encoding="utf-8") as tiedosto:
        tiedosto.write(tunnus + "\n")


def lataa_loput():
    
    try:
        with open(TIEDOSTO, "r", encoding="utf-8") as tiedosto:
            return {rivi.strip() for rivi in tiedosto if rivi.strip()}
    except FileNotFoundError:
        return set()


# ---------- Apufunktio ----------

def kysy_valinta(kysymys, vaihtoehdot):
    while True:
        print(f"\n{kysymys}")
        for numero, teksti in enumerate(vaihtoehdot, start=1):
            print(f"  {numero}) {teksti}")
        vastaus = input("> ").strip()
        if vastaus.isdigit() and 1 <= int(vastaus) <= len(vaihtoehdot):
            return int(vastaus)
        print("Anna numero listasta.")


# ---------- Kolme pakoreittiä (palauttavat True, jos pako onnistuu) ----------

def reitti_vartija(jeffrey):
    print("\n--- Suunnitelma: naamioidu vartijaksi ---")
    paikat = { 
        "pyykkihuone": "univormu",
        "naulakko": "lakki",
        "vahtimestarin pöytä": "kulkukortti",
    }
    nimet = list(paikat)
    while len(jeffrey.esineet) < 3:
        paikka = nimet[kysy_valinta("Minne Jeffrey hiipii hakemaan vermeitä?", nimet) - 1]
        esine = paikat[paikka]
        if esine in jeffrey.esineet:
            print("Täältä on jo haettu kaikki tarpeellinen.")
        else:
            jeffrey.esineet.append(esine)
            print(f"Jeffrey löytää paikasta {paikka}: {esine}")
    print("\nJeffreyn reppu:")
    jeffrey.nayta_reppu()

    vartija = Vartija("Vartija Virtanen", 6)
    for portti in range(1, 4):
        print(f"\nJeffrey kävelee portille {portti}/3.")
        if vartija.huomaako(True):
            vartija.puhu("Hetkinen, etkö sinä ole uusi?")
            valinta = kysy_valinta("Mitä Jeffrey tekee?", ["Tervehtii reippaasti", "Juoksee karkuun"])
            if valinta == 2 or random.random() < 0.3:
                print("Vartija ei uskonut. Jeffrey viedään takaisin selliin.")
                jeffrey.esineet.clear() 
                return False
            print("Vartija nyökkää ja päästää Jeffreyn läpi.")
        else:
            print("Kukaan ei kiinnitä huomiota. Portti aukeaa.")
    return True


def reitti_kierratys(jeffrey):
    print("\n--- Suunnitelma: kierrätysauto ---")
    print("Jeffrey saa työtehtäväksi lajitella vankilan jätteet. Jos lajittelu")
    print("onnistuu, hän voi piiloutua paperinkeräyslaatikkoon ja auto vie hänet pois.")
    lajit = ("lasi", "paperi", "metalli", "bio")
    jate = {
        "lasipullo": "lasi",
        "sanomalehti": "paperi",
        "säilyketölkki": "metalli",
        "banaanin kuori": "bio",
    }
    virheet = 0
    for esine, oikea in jate.items():
        vastaus = lajit[kysy_valinta(f"Mihin laatikkoon: {esine}?", lajit) - 1]
        if vastaus == oikea:
            print("Oikein! Maapallo kiittää.")
        else:
            virheet += 1
            print(f"Hups, {esine} kuuluu laatikkoon '{oikea}'. Virheitä: {virheet}/3")
        if virheet >= 3:
            print("Vartija huomaa sotkun ja epäilee Jeffreytä. Pako epäonnistui.")
            return False
    print("\nLajittelu onnistui! Jeffrey piiloutuu paperilaatikkoon.")
    print("Kierrätysauto hurisee portista ulos...")
    return True


def reitti_katto(jeffrey):
    print("\n--- Suunnitelma: katon kautta taivaaseen ---")
    print("Jeffrey kiinnittää köyden kattoputkeen.")
    return True


# ---------- Peli ja valikko ----------

REITIT = {"vartija": reitti_vartija, "kierratys": reitti_kierratys, "taivas": reitti_katto}


def nayta_ohjeet():
    print("\nJeffrey on vankilassa ja haluaa vapaaksi. Valitse numeroita")
    print("ja yritä päästä ulos. Löydätkö kaikki kolme pakotietä?")


def nayta_loput():
    loydetyt = lataa_loput()
    print(f"\nLöydetyt pakotiet: {len(loydetyt)}/{len(LOPUT)}")
    for tunnus, (nimi, _) in LOPUT.items():
        merkki = "x" if tunnus in loydetyt else " "
        print(f" [{merkki}] {nimi}")


def pelaa():
    jeffrey = Pelaaja("Jeffrey")
    print("\nJeffrey istuu sellissään. Tänään on hänen viimeinen päivänsä sisällä!")
    tunnukset = list(LOPUT)
    nimet = [LOPUT[t][0] for t in tunnukset]
    while True:
        tunnus = tunnukset[kysy_valinta("Valitse pakosuunnitelma:", nimet) - 1]
        if REITIT[tunnus](jeffrey):
            print(f"\n*** {LOPUT[tunnus][1]} ***")
            tallenna_loppu(tunnus)
            return
        print("\nPako epäonnistui. Jeffrey palaa selliin miettimään uutta suunnitelmaa.")


def main():
    print("=== JEFFREYN PAKO ===")
    while True:
        valinta = kysy_valinta("Päävalikko", VALIKKO)
        if valinta == 1:
            pelaa()
        elif valinta == 2:
            nayta_ohjeet()
        elif valinta == 3:
            nayta_loput()
        else:
            print("Kiitos pelaamisesta!")
            break


if __name__ == "__main__":
    main()
