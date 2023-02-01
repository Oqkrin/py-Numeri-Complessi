from NumeroComplesso import NumeroComplesso as z


class OperazioniTrigonometricheNC:

    @staticmethod
    def prodottoTrigonometrico(ax, by):
        return z(usaCoordinatePolari=True, r=ax.modulo * by.modulo, ia=ax.angolo + by.angolo)

    @staticmethod
    def quozienteTrigonometrico(ax, by):
        return z(usaCoordinatePolari=True, r=ax.modulo / by.modulo, ia=ax.angolo - by.angolo)
