import math

import NumeroComplesso as Z

class OperazioniNumeriComplessi:
    # avendo a + ix e b + iy
    # somma = a+b + i(x+y)
    @staticmethod
    def sommaComplessa(ax, by):
        parteReale = ax.getParteReale() + by.getParteReale()
        parteImmaginaria = ax.getParteImmaginaria() + by.getParteImmaginaria()
        return Z.NumeroComplesso(r=parteReale, ia=parteImmaginaria)

    @staticmethod
    def diffrenzaComplessa(ax, by):
        parteReale = ax.getParteReale() - by.getParteReale()
        parteImmaginaria = ax.getParteImmaginaria() - by.getParteImmaginaria()
        return Z.NumeroComplesso(r=parteReale, ia=parteImmaginaria)

    # prodotto = a*b - x*y + i(b*x + a*y)
    @staticmethod
    def prodottoComplesso(ax, by):
        parteReale = ax.getParteReale() * by.getParteReale() - ax.getParteImmaginaria() * by.getParteImmaginaria()
        parteImmaginaria = by.getParteReale() * ax.getParteImmaginaria() + ax.getParteReale() * by.getParteImmaginaria()
        return Z.NumeroComplesso(parteReale, parteImmaginaria)

    # quoziente = (a + ix / b + iy) * (coniugato del divisore/coniugato del
    # divisore) cioè (b - ix/b - ix)
    # il dividendo è un normale prodotto tra numeri complessi
    # il divisore è la somma per differenza del numero complesso quindi b^2 - y^2 *
    # (i^2 che è uguale a -1)
    # verificare che il divisore sia diverso da zeri
    @staticmethod
    def quozienteComplesso(ax, by):
        dividendo = OperazioniNumeriComplessi.prodottoComplesso(ax, by.getConiugato())
        divisore = Z.NumeroComplesso(math.pow(by.getConiugato().getParteImmaginaria(), 2) - math.pow(by.getParteReale(), 2), 0)
        if divisore.getParteReale() == 0:
            print("\033[1;31;40m Divisore Pari a Zero")
            divisore = Z.NumeroComplesso(1, 0)
        return dividendo
