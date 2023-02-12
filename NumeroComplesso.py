import math
from numpy import sign


class NumeroComplesso:
    __ft = "{modulo} ( cos({angolo}) + i sin({angolo}) )"
    __fa = "{parteReale} + i({parteImmaginaria})"
    __segnoParteReale = 1
    __segnoParteImmaginario = 1

    def __init__(self, r, ia, usaCoordinatePolari=False, usaRadianti=False):
        self.__controlloIstanzione(r=r, ia=ia, usaCoordinatePolari=usaCoordinatePolari, usaRadianti=usaRadianti)

    def __controlloIstanzione(self, r, ia, usaCoordinatePolari=False, usaRadianti=False):
        if usaCoordinatePolari:
            self.modulo = r
            self.angolo = ia if usaRadianti else math.radians(ia)
            self.parteReale = self.getParteReale()
            self.parteImmaginaria = self.getParteImmaginaria()
        else:
            self.parteReale = r
            self.__segnoParteReale = sign(r)
            self.parteImmaginaria = ia
            self.__segnoParteImmaginario = sign(ia)
            self.modulo = self.getModulo()
            self.angolo = self.getAngolo()

    def getParteReale(self):
        return self.modulo * math.cos(self.angolo) * self.__segnoParteReale

    def setParteReale(self, parteReale):
        self.__controlloIstanzione(r=parteReale, ia=self.parteImmaginaria)

    def getParteImmaginaria(self):
        return self.modulo * math.sin(self.angolo) * self.__segnoParteImmaginario

    def setParteImmaginaria(self, parteImmaginaria):
        self.__controlloIstanzione(r=self.parteReale, ia=parteImmaginaria)

    def getFormaAlgebrica(self):
        prNulla = self.getParteReale() == 0
        piNulla = self.getParteImmaginaria() == 0

        if prNulla and piNulla:
            return str(0)
        elif prNulla:
            return "i" + str(self.getParteImmaginaria())
        elif piNulla:
            return str(self.getParteReale())
        else:
            return self.__fa.format(parteReale=self.getParteReale(), parteImmaginaria=self.getParteImmaginaria())

    def getFormaTrigonometrica(self):
        return self.__ft.format(modulo=self.getModulo(), angolo=self.getAngolo())

    def getConiugato(self):
        return NumeroComplesso(self.parteReale, -self.parteImmaginaria)

    # modulo = pitagora cioè radice quadrata di (a^2 + x^2)
    def getModulo(self):
        return round(float(math.sqrt(math.pow(self.parteReale, 2) + math.pow(self.parteImmaginaria, 2))), 3)

    def setModulo(self, modulo):
        self.__controlloIstanzione(r=modulo, ia=self.angolo, usaCoordinatePolari=True)

    def getAngolo(self):
        return 0 if self.parteReale == 0 else math.atan(self.parteImmaginaria / self.parteReale)

    def setAngolo(self, angolo):
        self.__controlloIstanzione(r=self.modulo, ia=angolo, usaCoordinatePolari=True)

    def getGradi(self):
        return math.degrees(self.getAngolo())

    def setRadianti(self, radianti):
        self.__controlloIstanzione(r=self.modulo, ia=radianti, usaCoordinatePolari=True, usaRadianti=True)
