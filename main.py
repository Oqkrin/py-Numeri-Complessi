import OperazioniAlgebricheNC as oanc
from NumeroComplesso import NumeroComplesso


def main():
    print(oanc.quozienteComplesso(NumeroComplesso(1, 0), NumeroComplesso(0, 1)).getFormaAlgebrica())


if __name__ == "__main__":
    main()


def controlloInput(inputText):
    var = None
    while 1:
        try:
            var = float(input(inputText))
            break
        except ValueError:
            print("\ninput errato riprovare")
            continue
    return int(var) if var.is_integer() else float(var)
