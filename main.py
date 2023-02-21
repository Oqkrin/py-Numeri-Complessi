from NumeroComplesso import NumeroComplesso as z, IorD
from decimal import Decimal as dec
import OperazioniAlgebricheNC as oanc
import OperazioniTrigonometricheNC as otnc
from InterfacciaGrafica import Interfaccia as gui


def controlloInput(inputText):
    var = None
    while 1:
        try:
            var = float(input(inputText))
            break
        except ValueError:
            print("\ninput errato riprovare")
            continue
    return IorD(var)


def main():
    interfaccia = gui()


if __name__ == "__main__":
    main()
