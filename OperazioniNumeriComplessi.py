import math
from NumeroComplesso import NumeroComplesso as z


class OperazioniNumeriComplessi:
    # avendo a + ix e b + iy
    # somma = a+b + i(x+y)
    @staticmethod
    def sommaComplessa(ax, by):
        parteReale = ax.getParteReale() + by.getParteReale()
        parteImmaginaria = ax.getParteImmaginaria() + by.getParteImmaginaria()
        return z(r=parteReale, ia=parteImmaginaria)

    @staticmethod
    def differenzaComplessa(ax, by):
        parteReale = ax.getParteReale() - by.getParteReale()
        parteImmaginaria = ax.getParteImmaginaria() - by.getParteImmaginaria()
        return z(r=parteReale, ia=parteImmaginaria)

    # prodotto = a*b - x*y + i(b*x + a*y)
    @staticmethod
    def prodottoComplesso(ax, by):
        parteReale = ax.getParteReale() * by.getParteReale() - ax.getParteImmaginaria() * by.getParteImmaginaria()
        parteImmaginaria = by.getParteReale() * ax.getParteImmaginaria() + ax.getParteReale() * by.getParteImmaginaria()
        return z(parteReale, parteImmaginaria)

    # quoziente = (a + ix / b + iy) * (coniugato del divisore/coniugato del
    # divisore) cioè (b - ix/b - ix)
    # il dividendo è un normale prodotto tra numeri complessi
    # il divisore è la somma per differenza del numero complesso quindi b^2 - y^2 *
    # (i^2 che è uguale a -1)
    # verificare che il divisore sia diverso da zeri
    @staticmethod
    def quozienteComplesso(ax, by):
        dividendo = OperazioniNumeriComplessi.prodottoComplesso(ax, by.getConiugato())
        divisore = OperazioniNumeriComplessi.sommaPerDifferenza(by)
        if divisore == 0:
            print("\033[1;31;40m Divisore Pari a Zero")
            return z(0, 0)
        else:
            return z(dividendo.parteReale/divisore, dividendo.parteImmaginaria/divisore)

    @staticmethod
    def sommaPerDifferenza(by):
        return math.pow(by.getConiugato().getParteImmaginaria(), 2) - math.pow(by.getParteReale(), 2)
