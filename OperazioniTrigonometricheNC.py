import numpy
import numpy as np
from NumeroComplesso import NumeroComplesso as z, tIoD
import OperazioniAlgebricheNC as oanc
from decimal import Decimal as dec


def prodottoTrigonometrico(ax, by):
    return z(usaCoordinatePolari=True, usaRadianti=True, r=ax.modulo * by.modulo, ia=ax.angolo + by.angolo)


def quozienteTrigonometrico(ax, by):
    return z(usaCoordinatePolari=True, usaRadianti=True, r=tIoD(ax.modulo) / tIoD(by.modulo),
             ia=ax.angolo - by.angolo)


def elevamentoTrigonmetrico(ax, e):
    if ax.parteReale != 0:
        match np.sign(e):
            case 1:
                return z(usaCoordinatePolari=True, usaRadianti=True, r=ax.modulo ** e, ia=e * ax.angolo)
            case -1:
                return z(usaCoordinatePolari=True, usaRadianti=True, r=ax.modulo ** e, ia=-e * ax.angolo).getConiugato()
            case _:
                return z(1, 0)
    else:
        # elevamento parte immaginaria
        ax.setParteImmaginaria(ax.parteImmaginaria ** e)
        # gestione i
        match e % 4:
            case -4:
                return z(1 * ax.parteImmaginaria, 0)
            case -3:
                return z(0, 1 * ax.parteImmaginaria)
            case -2:
                return z(-1 * ax.parteImmaginaria, 0)
            case -1:
                return z(0, -1 * ax.parteImmaginaria)
            case 0:
                return z(1 * ax.parteImmaginaria, 0)
            case 1:
                return z(0, 1 * ax.parteImmaginaria)
            case 2:
                return z(-1 * ax.parteImmaginaria, 0)
            case 3:
                return z(0, -1 * ax.parteImmaginaria)
            case 4:
                return z(1 * ax.parteImmaginaria, 0)


def radiceTrigonometrica(ax, n):
    radici = []
    for k in range(0, n):
        radici.append(
            prodottoTrigonometrico(ax=z(usaCoordinatePolari=True, usaRadianti=True, r=tIoD(ax.modulo) ** (1 / tIoD(n)),
                                        ia=tIoD(ax.angolo + k * 2 * np.pi) / tIoD(n)),
                                   by=z(1, 0) if n % 2 == 0 else z(-1, 0)))
    return radici
