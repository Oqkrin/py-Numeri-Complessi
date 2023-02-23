import decimal
import math
from numpy import sign, pi
from decimal import Decimal as dec


def IorD(i):
    """
    converte valore in decimale o intero per maggiore precisione
    :param i:
    :return: valore convertito in int o decimale
    """
    return i if i.__class__ == decimal.Decimal else int(i) if float(i).is_integer() else dec(str(i))


class NumeroComplesso:
    __ft = "{modulo} (cos({angolo}) + i sin({angolo}))"
    __fa = "{r} {sgn}{i}i"
    __segnoParteReale = 1
    __segnoParteImmaginario = 1

    def __init__(self, r, ia, usaCoordinatePolari=False, usaRadianti=False):
        self.__controlloIstanzione(r=r, ia=ia, usaCoordinatePolari=usaCoordinatePolari, usaRadianti=usaRadianti)

    def __controlloIstanzione(self, r, ia, usaCoordinatePolari=False, usaRadianti=False):
        if usaCoordinatePolari:
            self.modulo = IorD(r)
            self.angolo = IorD(ia) if usaRadianti else IorD(math.radians(IorD(ia)))
            self.parteReale = IorD(self.calcParteReale())
            self.parteImmaginaria = IorD(self.calcParteImmaginaria())
        else:
            self.parteReale = IorD(r)
            self.parteImmaginaria = IorD(ia)
            self.modulo = IorD(self.calcModulo())
            self.angolo = IorD(self.calcAngolo())
        self.__segnoParteReale = sign(self.parteReale)
        self.__segnoParteImmaginario = sign(self.parteImmaginaria)

    def calcParteReale(self):
        """
        calcola la parte reale avendo modulo e angolo
        :return: parte reale
        """
        return self.modulo * IorD(math.cos(self.angolo)) * self.__segnoParteReale

    def calcParteImmaginaria(self):
        """
        calcola la parte immaginaria avendo modulo e angolo
        :return: parte immaginaria
        """
        return self.modulo * IorD(math.sin(self.angolo)) * self.__segnoParteImmaginario

    def calcModulo(self):
        """
        calcola il modulo avendo parte immaginaria e reale
        :return: modulo
        """
        return IorD(math.sqrt(self.parteReale ** 2 + self.parteImmaginaria ** 2))

    def calcAngolo(self):
        """
        calcola l'angolo conoscendo la tangente cioè cos/sin -> parte Immaginaria / parte reale
        :return: angolo in radianti
        """
        return IorD(pi) / 2 * self.__segnoParteImmaginario if self.parteReale == 0 else IorD(
            math.atan(IorD(self.parteImmaginaria)) / IorD(self.parteReale))

    def setModulo(self, modulo):
        self.__controlloIstanzione(r=modulo, ia=self.angolo, usaCoordinatePolari=True)

    def setGradi(self, angolo):
        self.__controlloIstanzione(r=self.modulo, ia=angolo, usaCoordinatePolari=True)

    def setRadianti(self, radianti):
        self.__controlloIstanzione(r=self.modulo, ia=radianti, usaCoordinatePolari=True, usaRadianti=True)

    def setParteReale(self, parteReale):
        self.__controlloIstanzione(r=parteReale, ia=self.parteImmaginaria)

    def setParteImmaginaria(self, parteImmaginaria):
        self.__controlloIstanzione(r=self.parteReale, ia=parteImmaginaria)

    def getGradi(self):
        return math.degrees(self.angolo)

    def getRadianti(self):
        return self.angolo

    def getFormAlgebrica(self):
        if self.parteReale == 0 and self.parteImmaginaria == 0:
            return str(0)
        elif self.parteReale == 0:
            return self.sIgn() if self.parteImmaginaria == self.__segnoParteImmaginario \
                else str(IorD(self.parteImmaginaria)) + "i"
        elif self.parteImmaginaria == 0:
            return str(IorD(self.parteReale))
        else:
            return self.__fa.format(r=IorD(self.parteReale),
                                    i=abs(IorD(self.parteImmaginaria)) if self.parteImmaginaria != 1 else " ",
                                    sgn=self.sIgn())

    def getFormTrigonometrica(self, usaRadianti=False):
        return self.__ft.format(modulo=self.modulo, angolo=self.angolo if usaRadianti else (str(self.getGradi()) + '°'))

    def sIgn(self):
        """
        ritorna il segno della parte immaginaria come stringa
        :return: segno parte immaginario come string
        """
        match self.__segnoParteImmaginario:
            case 1:
                return "+"
            case -1:
                return "-"
            case _:
                return "+"

    def getConiugato(self):
        return NumeroComplesso(self.parteReale, -self.parteImmaginaria)

    def uguale(self, ax):
        uguaglianzaAlgebrica = self.parteReale == ax.parteReale and self.parteImmaginaria == ax.parteImmaginaria
        uguaglianzaTrigonometrica = self.modulo == ax.modulo and self.angolo == ax.angolo
        return True if uguaglianzaAlgebrica or uguaglianzaTrigonometrica else False
