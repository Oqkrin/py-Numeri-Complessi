import math
from numpy import sign
from decimal import Decimal as dec


def tIoD(value):
    """
    parse value to int or decimal
    :param value:
    :return:
    """
    return int(value) if float(value).is_integer() else dec(str(value))


class NumeroComplesso:
    __ft = "{modulo} (cos({angolo}) + i sin({angolo}))"
    __fa = "{parteReale} {sgn}{parteImmaginaria}i"
    __segnoParteReale = 1
    __segnoParteImmaginario = 1

    def __init__(self, r, ia, usaCoordinatePolari=False, usaRadianti=False):
        self.__controlloIstanzione(r=r, ia=ia, usaCoordinatePolari=usaCoordinatePolari, usaRadianti=usaRadianti)

    def __controlloIstanzione(self, r, ia, usaCoordinatePolari=False, usaRadianti=False):
        if usaCoordinatePolari:
            self.modulo = tIoD(r)
            self.angolo = tIoD(ia) if usaRadianti else tIoD(math.radians(ia))
            self.parteReale = tIoD(self.calcParteReale())
            self.parteImmaginaria = tIoD(self.calcParteImmaginaria())
        else:
            self.parteReale = tIoD(r)
            self.__segnoParteReale = sign(r)
            self.parteImmaginaria = tIoD(ia)
            self.__segnoParteImmaginario = sign(ia)
            self.modulo = tIoD(self.calcModulo())
            self.angolo = tIoD(self.calcAngolo())

    def calcParteReale(self):
        return self.modulo * tIoD(math.cos(self.angolo)) * self.__segnoParteReale

    def setParteReale(self, parteReale):
        self.__controlloIstanzione(r=parteReale, ia=self.parteImmaginaria)

    def calcParteImmaginaria(self):
        return self.modulo * tIoD(math.sin(self.angolo)) * self.__segnoParteImmaginario

    def setParteImmaginaria(self, parteImmaginaria):
        self.__controlloIstanzione(r=self.parteReale, ia=parteImmaginaria)

    def getFormaAlgebrica(self):
        if self.parteReale == 0 and self.parteImmaginaria == 0:
            return str(0)
        elif self.parteReale == 0:
            return self.segn() if self.parteImmaginaria == self.__segnoParteImmaginario else str(tIoD(self.parteImmaginaria)) + "i"
        elif self.parteImmaginaria == 0:
            return str(tIoD(self.parteReale))
        else:
            return self.__fa.format(parteReale=tIoD(self.parteReale),
                                    parteImmaginaria=abs(tIoD(self.parteImmaginaria)) if self.parteImmaginaria != 1 else " ",
                                    sgn=self.segn())

    def getFormaTrigonometrica(self, usaRadianti=False):
        return self.__ft.format(modulo=self.modulo, angolo=self.angolo if usaRadianti else self.getGradi())

    def getConiugato(self):
        return NumeroComplesso(self.parteReale, -self.parteImmaginaria)

    # modulo = pitagora cioè radice quadrata di (a^2 + x^2)
    def calcModulo(self):
        mod = math.sqrt(self.parteReale ** 2 + self.parteImmaginaria ** 2)
        return int(mod) if mod.is_integer() else dec(mod)

    def setModulo(self, modulo):
        self.__controlloIstanzione(r=modulo, ia=self.angolo, usaCoordinatePolari=True)

    def calcAngolo(self):
        return 0 if self.parteReale == 0 else tIoD(math.atan(tIoD(self.parteImmaginaria)) / tIoD(self.parteReale))

    def setAngolo(self, angolo):
        self.__controlloIstanzione(r=self.modulo, ia=angolo, usaCoordinatePolari=True)

    def getGradi(self):
        return math.degrees(self.angolo)

    def setRadianti(self, radianti):
        self.__controlloIstanzione(r=self.modulo, ia=radianti, usaCoordinatePolari=True, usaRadianti=True)

    def segn(self):
        match self.__segnoParteImmaginario:
            case 1:
                return "+"
            case -1:
                return "-"
            case _:
                return "+"

    def uguale(self, ax):
        if (self.parteReale == ax.parteReale and self.parteImmaginaria == ax.parteImmaginaria) or \
                (self.modulo == ax.modulo and self.angolo == ax.angolo):
            return True
        else:
            return False
