from NumeroComplesso import NumeroComplesso as z, IorD
from OperazioniTrigonometricheNC import prodottoTrigonometrico


# avendo a + ix e b + iy
# somma = a+b + i(x+y)
def sommaComplessa(ax, by):
    parteReale = ax.parteReale + by.parteReale
    parteImmaginaria = ax.parteImmaginaria + by.parteImmaginaria
    return z(r=parteReale, ia=parteImmaginaria)


def differenzaComplessa(ax, by):
    parteReale = ax.parteReale - by.parteReale
    parteImmaginaria = ax.parteImmaginaria - by.parteImmaginaria
    return z(r=parteReale, ia=parteImmaginaria)


# avendo a + ix * b + iy il prodotto è uguale a :
# prodotto = a*b - x*y + i(b*x + a*y)
def prodottoComplesso(ax, by):
    parteReale = ax.parteReale * by.parteReale - ax.parteImmaginaria * by.parteImmaginaria
    parteImmaginaria = by.parteReale * ax.parteImmaginaria + ax.parteReale * by.parteImmaginaria
    return z(parteReale, parteImmaginaria)


# quoziente = (a + ix / b + iy) * (coniugato del divisore/coniugato del
# divisore) cioè (b - ix/b - ix)
# il dividendo è un normale prodotto tra numeri complessi
# il divisore è la somma per differenza del numero complesso quindi b^2 - y^2 *
# (i^2 che è uguale a -1)
# verificare che il divisore sia diverso da zeri
def quozienteComplesso(ax, by):
    dividendo = prodottoComplesso(ax, by.getConiugato())
    divisore = prodottoComplesso(by, by.getConiugato()).parteReale
    if divisore == 0:
        return prodottoTrigonometrico(ax, by)
    else:
        return z(IorD(dividendo.parteReale) / IorD(divisore), IorD(dividendo.parteImmaginaria) / IorD(divisore))
