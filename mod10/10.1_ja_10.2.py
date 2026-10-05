class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros 

    def siirry_kerrokseen(self, kohde):
        if kohde < self.alin_kerros or kohde > self.ylin_kerros:
            print(f"Kerrosta {kohde} ei ole olemassa.")
            return
        while self.kerros < kohde:
            self.kerros_ylös()
        while self.kerros > kohde:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print(f"Hissi on nyt kerroksessa {self.kerros}.")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.kerros}.")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for _ in range(hissien_lkm):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print(f"Hissiä numero {hissin_numero} ei ole olemassa.")
            return
        print(f"Ajetaan hissiä {hissin_numero}:")
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohde_kerros)



h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)


talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 6)
talo.aja_hissiä(2, 4)
talo.aja_hissiä(1, 1)
talo.aja_hissiä(2, 1)