from numpy import sign
from NumeroComplesso import NumeroComplesso as z


def prodottoTrigonometrico(ax, by):
    return z(usaCoordinatePolari=True, r=ax.modulo * by.modulo, ia=ax.angolo + by.angolo)


def quozienteTrigonometrico(ax, by):
    return z(usaCoordinatePolari=True, r=ax.modulo / by.modulo, ia=ax.angolo - by.angolo)


def elevamentoTrigonmetrico(ax, e):
    match sign(e):
        case 1:
            return z(usaCoordinatePolari=True, r=pow(ax.modulo, e), ia=e * ax.angolo)
        case -1:
            return z(usaCoordinatePolari=True, r=pow(ax.modulo, e), ia=-e * ax.angolo).getConiugato()
        case _:
            return z(1, 0)
