from NumeroComplesso import NumeroComplesso
from OperazioniAlgebricheNC import OperazioniNumeriComplessi as oanc

a = float(input("Digita parte reale del primo valore : "))
x = float(input("Digita parte immaginaria del primo valore : "))
b = float(input("Digita parte reale del secondo valore : "))
y = float(input("Digita parte immaginaria del secondo valore : "))

ax = NumeroComplesso(a, x)
by = NumeroComplesso(b, y)

print("Forma Algebrica ax : " + ax.getFormaTrigonometrica())
print("Forma Algebrica by : " + by.getFormaTrigonometrica() + "\n")
print("Forma Trigonometrica ax : " + ax.getNumeroComplesso())
print("Forma Trigonometrica by : " + by.getNumeroComplesso() + "\n")
print("coniugato ax : " + ax.getConiugato().getNumeroComplesso())
print("coniugato by : " + by.getConiugato().getNumeroComplesso() + "\n")
print("modulo ax : " + str(ax.getModulo()))
print("modulo by : " + str(by.getModulo()) + "\n")
print("Somma : " + oanc.sommaComplessa(ax=ax, by=by).getNumeroComplesso() + "\n")
print("differenza ax - by : " + oanc.differenzaComplessa(ax=ax, by=by).getNumeroComplesso())
print("differenza by - ax : " + oanc.differenzaComplessa(ax=by, by=ax).getNumeroComplesso() + "\n")
print("prodotto : " + oanc.prodottoComplesso(ax=ax, by=by).getNumeroComplesso() + "\n")
print("quoziente ax/by : " + oanc.quozienteComplesso(ax=ax, by=by).getNumeroComplesso())
print("quoziente by/ax : " + oanc.quozienteComplesso(ax=by, by=ax).getNumeroComplesso())
