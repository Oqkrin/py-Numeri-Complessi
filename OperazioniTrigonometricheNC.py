import numpy as np
from NumeroComplesso import NumeroComplesso as z, IorD


def prodottoTrigonometrico(ax, by):
    return z(usaCoordinatePolari=True, usaRadianti=True, r=ax.modulo * by.modulo, ia=ax.angolo + by.angolo)


def quozienteTrigonometrico(ax, by):
    return z(usaCoordinatePolari=True, usaRadianti=True, r=IorD(ax.modulo) / IorD(by.modulo), ia=ax.angolo - by.angolo)


def elevamentoTrigonmetrico(ax, e):
    if ax.parteReale != 0:
        match np.sign(e):
            case 1:
                return z(usaCoordinatePolari=True, usaRadianti=True, r=ax.modulo ** e, ia=e * ax.angolo)
            case -1:
                return z(usaCoordinatePolari=True, usaRadianti=True, r=ax.modulo ** e, ia=-e * ax.angolo).getConiugato()
            case _:
                return z(r=1)
    else:
        # elevamento parte immaginaria
        ax.setParteImmaginaria(ax.parteImmaginaria ** e)
        # gestione i
        match e % 4:
            case -4:
                return z(r=1 * ax.parteImmaginaria)
            case -3:
                return z(ia=1 * ax.parteImmaginaria)
            case -2:
                return z(r=-1 * ax.parteImmaginaria)
            case -1:
                return z(ia=-1 * ax.parteImmaginaria)
            case 0:
                return z(r=1 * ax.parteImmaginaria)
            case 1:
                return z(ia=1 * ax.parteImmaginaria)
            case 2:
                return z(r=-1 * ax.parteImmaginaria)
            case 3:
                return z(ia=-1 * ax.parteImmaginaria)
            case 4:
                return z(r=1 * ax.parteImmaginaria)


def radiceTrigonometrica(ax, ir):
    radici = []
    for k in range(0, ir):
        radici.append(z(usaCoordinatePolari=True, usaRadianti=True,
                        r=IorD(ax.modulo) ** (1 / IorD(ir)),
                        ia=IorD(ax.angolo + k * 2 * IorD(np.pi)) / IorD(ir)))
    return tuple(radici)
