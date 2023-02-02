import math

from numpy import sign


class NumeroComplesso:
    formaTrigonometrica = "{modulo} ( cos({angolo}) + i sin({angolo}) )"
    formaNormale = "{parteReale} + i({parteImmaginaria})"
    segnoParteReale = 1
    segnoParteImmaginario = 1

    def __init__(self, r, ia, usaCoordinatePolari=False, usaRadianti=False):
        self.__controlloIstanzione(r=r, ia=ia, usaCoordinatePolari=usaCoordinatePolari, usaRadianti=usaRadianti)

    def __controlloIstanzione(self, r, ia, usaCoordinatePolari=False, usaRadianti=False):
        if usaCoordinatePolari:
            self.modulo = r
            self.angolo = ia if usaRadianti else math.degrees(ia)
            self.parteReale = self.getParteReale()
            self.parteImmaginaria = self.getParteImmaginaria()
        else:
            self.parteReale = r
            self.segnoParteReale = sign(ia)
            self.parteImmaginaria = ia
            self.segnoParteImmaginario = sign(ia)
            self.modulo = self.getModulo()
            self.angolo = self.getAngolo()

    def getParteReale(self):
        return self.modulo * math.cos(self.angolo) * self.segnoParteReale

    def setParteReale(self, parteReale):
        self.__controlloIstanzione(r=parteReale, ia=self.parteImmaginaria)

    def getParteImmaginaria(self):
        return self.modulo * math.sin(self.angolo) * self.segnoParteImmaginario

    def setParteImmaginaria(self, parteImmaginaria):
        self.__controlloIstanzione(r=self.parteReale, ia=parteImmaginaria)

    def getNumeroComplesso(self):
        return self.formaNormale.format(parteReale=self.getParteReale(), parteImmaginaria=self.getParteImmaginaria())

    def getFormaTrigonometrica(self):
        return self.formaTrigonometrica.format(modulo=self.getModulo(), angolo=self.getAngolo())

    def getConiugato(self):
        return NumeroComplesso(self.parteReale, -self.parteImmaginaria)

    # modulo = pitagora cioè radice quadrata di (a^2 + x^2)
    def getModulo(self):
        return float(math.sqrt(math.pow(self.parteReale, 2) + math.pow(self.parteImmaginaria, 2)))

    def setModulo(self, modulo):
        self.__controlloIstanzione(r=modulo, ia=self.angolo, usaCoordinatePolari=True)

    def getAngolo(self):
        return 0 if self.parteReale == 0 else math.atan(self.parteImmaginaria/self.parteReale)

    def setAngolo(self, angolo):
        self.__controlloIstanzione(r=self.modulo, ia=angolo, usaCoordinatePolari=True)

    def getRadianti(self):
        return math.radians(self.getAngolo())

    def setRadianti(self, radianti):
        self.__controlloIstanzione(r=self.modulo, ia=radianti, usaCoordinatePolari=True, usaRadianti=True)
