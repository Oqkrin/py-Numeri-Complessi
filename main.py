from NumeroComplesso import NumeroComplesso
from OperazioniNumeriComplessi import OperazioniNumeriComplessi

a = float(input("Digita parte reale del primo valore : "))
x = float(input("Digita parte immaginaria del primo valore : "))
b = float(input("Digita parte reale del secondo valore : "))
y = float(input("Digita parte immaginaria del secondo valore : "))

ax = NumeroComplesso(a, x)
by = NumeroComplesso(b, y)

print("coniugato ax : " + ax.getConiugato().getNumeroComplesso())
print("coniugato by : " + by.getConiugato().getNumeroComplesso())
print("\nmodulo ax : " + ax.getModulo())
print("modulo by : " + by.getModulo())
print("modulo by : " + by.getModulo())
print("modulo by : " + by.getModulo())
print("\nSomma : " + OperazioniNumeriComplessi.sommaComplessa(ax, by).getNumeroComplesso())
print("\ndifferenza ax - by : "+ OperazioniNumeriComplessi.diffrenzaComplessa(ax, by).getNumeroComplesso())
print("differenza by - ax : "+ OperazioniNumeriComplessi.diffrenzaComplessa(by, ax).getNumeroComplesso())
print("\nprodotto : " + OperazioniNumeriComplessi.prodottoComplesso(ax, by).getNumeroComplesso())
print("\nquoziente ax/by : " + OperazioniNumeriComplessi.quozienteComplesso(ax, by).getNumeroComplesso())
print("quoziente by/ax : " + OperazioniNumeriComplessi.quozienteComplesso(by, ax).getNumeroComplesso())