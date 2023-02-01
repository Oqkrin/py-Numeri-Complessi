from numpy import sign
from NumeroComplesso import NumeroComplesso as z


class OperazioniTrigonometricheNC:

    @staticmethod
    def prodottoTrigonometrico(ax, by):
        return z(usaCoordinatePolari=True, r=ax.modulo * by.modulo, ia=ax.angolo + by.angolo)

    @staticmethod
    def quozienteTrigonometrico(ax, by):
        return z(usaCoordinatePolari=True, r=ax.modulo / by.modulo, ia=ax.angolo - by.angolo)

    @staticmethod
    def elevamentoTrigonmetrico(ax, e):
        match sign(e):
            case 1: return z(usaCoordinatePolari=True, r=pow(ax.modulo, e), ia=e*ax.angolo)
            case -1: return z(usaCoordinatePolari=True, r=pow(ax.modulo, e), ia=e*ax.angolo)
            case _: return 1
