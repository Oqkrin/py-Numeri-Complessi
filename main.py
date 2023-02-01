from NumeroComplesso import NumeroComplesso
from OperazioniNumeriComplessi import OperazioniNumeriComplessi

a = float(input("Digita parte reale del primo valore : "))
x = float(input("Digita parte immaginaria del primo valore : "))
b = float(input("Digita parte reale del secondo valore : "))
y = float(input("Digita parte immaginaria del secondo valore : "))

ax = NumeroComplesso(a, x)
by = NumeroComplesso(b, y)

print("coniugato ax : " + ax.getConiugato().getNumeroComplesso())
print("coniugato by : " + by.getConiugato().getNumeroComplesso() + "\n")
print("modulo ax : " + str(ax.getModulo()))
print("modulo by : " + str(by.getModulo()) + + "\n")
print("Somma : " + OperazioniNumeriComplessi.sommaComplessa(ax, by).getNumeroComplesso() + "\n")
print("differenza ax - by : " + OperazioniNumeriComplessi.differenzaComplessa(ax, by).getNumeroComplesso())
print("differenza by - ax : " + OperazioniNumeriComplessi.differenzaComplessa(by, ax).getNumeroComplesso() + "\n")
print("prodotto : " + OperazioniNumeriComplessi.prodottoComplesso(ax, by).getNumeroComplesso() + "\n")
print("quoziente ax/by : " + OperazioniNumeriComplessi.quozienteComplesso(ax, by).getNumeroComplesso())
print("quoziente by/ax : " + OperazioniNumeriComplessi.quozienteComplesso(by, ax).getNumeroComplesso())
