import math

import OperazioniAlgebricheNC as oanc
from NumeroComplesso import NumeroComplesso as z
from decimal import Decimal as dec


def toINTorDEC(value):
    return int(value) if value.is_integer() else dec(str(value))


def controlloInput(inputText):
    var = None
    while 1:
        try:
            var = float(input(inputText))
            break
        except ValueError:
            print("\ninput errato riprovare")
            continue
    return toINTorDEC(var)


def main():
    print(
        oanc.sommaComplessa(
            z(math.sqrt(2), -1),
            oanc.prodottoComplesso(z(0, -1), z(1, -math.sqrt(2)))
        )
        .getFormaAlgebrica()
    )


if __name__ == "__main__":
    main()
