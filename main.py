import OperazioniAlgebricheNC as oanc
import OperazioniTrigonometricheNC as otnc
from NumeroComplesso import NumeroComplesso
from fractions import Fraction as fra


def repertorio(ax, by, eax, eby):
    print("\nForma Algebrica ax : " + ax.getFormaAlgebrica())
    print("Forma Algebrica by : " + by.getFormaAlgebrica() + "\n")

    print("Forma Trigonometrica ax : " + ax.getFormaTrigonometrica())
    print("Forma Trigonometrica by : " + by.getFormaTrigonometrica() + "\n")

    print("coniugato ax : " + ax.getConiugato().getFormaAlgebrica())
    print("coniugato by : " + by.getConiugato().getFormaAlgebrica() + "\n")

    print("modulo ax : " + str(ax.calcModulo()))
    print("modulo by : " + str(by.calcModulo()) + "\n")

    print("Somma : " + oanc.sommaComplessa(ax=ax, by=by).getFormaAlgebrica() + "\n")

    print("differenza ax - by : " + oanc.differenzaComplessa(ax=ax, by=by).getFormaAlgebrica())
    print("differenza by - ax : " + oanc.differenzaComplessa(ax=by, by=ax).getFormaAlgebrica() + "\n")

    print("prodotto : " + oanc.prodottoComplesso(ax=ax, by=by).getFormaAlgebrica())
    print("prodotto formaTrigonometrica : " + otnc.prodottoTrigonometrico(ax=ax, by=by).getFormaTrigonometrica() + "\n")

    print("quoziente ax/by : " + oanc.quozienteComplesso(ax=ax, by=by).getFormaAlgebrica())
    print("quoziente trigonometrica ax/by : " + otnc.quozienteTrigonometrico(ax=ax,
                                                                             by=by).getFormaTrigonometrica() + "\n")

    print("quoziente by/ax : " + oanc.quozienteComplesso(ax=by, by=ax).getFormaAlgebrica())
    print(
        "prodotto trigonometrica by/ax :" + otnc.quozienteTrigonometrico(ax=by, by=ax).getFormaTrigonometrica() + "\n")

    print("elevamento ax a " + str(eax) + ": " + otnc.elevamentoTrigonmetrico(ax=ax, e=eax).getFormaAlgebrica())
    print("elevamento by a " + str(eby) + ": " + otnc.elevamentoTrigonmetrico(ax=by, e=eby).getFormaAlgebrica() + "\n")

    print("radice ax a " + str(eax) + ": " + otnc.radiceTrigonometrica(ax=ax, n=eax).getFormaAlgebrica())
    print("radice by a " + str(eby) + ": " + otnc.radiceTrigonometrica(ax=by, n=eby).getFormaAlgebrica())


def controlloInput(inputText):
    var = None
    while 1:
        try:
            var = float(input(inputText))
            break
        except ValueError:
            print("\ninput errato riprovare")
            continue
    print(var.is_integer())
    return int(var) if var.is_integer() else float(var)


print(oanc.quozienteComplesso(NumeroComplesso(1, 0), NumeroComplesso(0, 1)).getFormaAlgebrica())

a = controlloInput("Digita parte reale del primo valore : ")
x = controlloInput("Digita parte immaginaria del primo valore : ")

b = controlloInput("Digita parte reale del secondo valore : ")
y = controlloInput("Digita parte immaginaria del secondo valore : ")

eax = controlloInput("Digita esponente primo numero : ")
eby = controlloInput("Digita esponente secondo numero : ")

ax = NumeroComplesso(a, x)
by = NumeroComplesso(b, y)

# repertorio(ax, by, eax, eby)

# TODO: arrotondamento 50% => usare frazioni
