class Nemoc:
    # poradi argumentu v radku nize si klidne preskladejte
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'Jmeno: {self.jmeno}'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti


class Koronavirus(Nemoc):
    def __init__ (self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        super().__init__(jmeno, inkubacni_doba, pocet_obeti, sireni)
        self.varianty = []

    def pridej_variantu(self, varianta):
        self.varianty.append(varianta)

    def __str__(self):
        if len (self.varianty) == 0 :
            text = super().__str__()
            text = text + f"(zadne nalezene varianty)"
            return text
        else:
            text = super().__str__()
            seznam = ', '.join(self.varianty)
            text = text + f" (varianty: {seznam})"
            return text
        

corona = Koronavirus('Coronavirus', 5, 100, 'vzduchem')
print (corona) 
corona.pridej_variantu('omikron')
print (corona) 
corona.pridej_variantu('delta')
print(corona)