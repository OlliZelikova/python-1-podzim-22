class Recept:
    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = int (narocnost)
        self.url_adresa = url_adresa
        self.vyzkouseno = False
    
    def __str__(self):
        if self.vyzkouseno == False:
            return f"{self.nazev} (narocnost: {self.narocnost}) - jeste nevyzkouseno"
        else: 
            return f"{self.nazev} (narocnost: {self.narocnost}) - vyzkouseno"

    def zmen_narocnost(self, nova_hodnota):
        self.narocnost = nova_hodnota

    def zkusit(self):
        self.vyzkouseno = True

tiramisu = Recept ("Tiramisu", 5, 'wwww')
tiramisu.zmen_narocnost('3')
tiramisu.zkusit
print (tiramisu)


class Kucharka:
    def __init__ (self, nazevkuch, autor):
        self.nazevkuch = nazevkuch
        self.autor = autor
        self.recepty = []

    def __str__(self):
        return f"{self.nazevkuch} od {self.autor} - {self.pocet_receptu()} receptu"
    

    def pridej_recept(self, recept):
        self.recepty.append(recept)

    
    def pocet_receptu (self):
        return len (self.recepty)

        
moje_kucharka = Kucharka('Dezerty', 'Andy')
moje_kucharka.pridej_recept(tiramisu)
print(moje_kucharka) 
print(moje_kucharka.pocet_receptu())