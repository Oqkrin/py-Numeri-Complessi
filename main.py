from NumeroComplesso import NumeroComplesso as z, tIoD
from decimal import Decimal as dec
import OperazioniAlgebricheNC as oanc
import OperazioniTrigonometricheNC as otnc
from InterfacciaGrafica import interfaccia


def controlloInput(inputText):
    var = None
    while 1:
        try:
            var = float(input(inputText))
            break
        except ValueError:
            print("\ninput errato riprovare")
            continue
    return tIoD(var)


def main():
    interfaccia = interfaccia()


if __name__ == "__main__":
    main()
