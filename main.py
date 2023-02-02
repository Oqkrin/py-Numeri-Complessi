from NumeroComplesso import NumeroComplesso
import OperazioniAlgebricheNC as oanc
import OperazioniTrigonometricheNC as otnc

a = float(input("Digita parte reale del primo valore : "))
x = float(input("Digita parte immaginaria del primo valore : "))
b = float(input("Digita parte reale del secondo valore : "))
y = float(input("Digita parte immaginaria del secondo valore : "))
eax = int(input("Digita esponente primo numero : "))
eby = int(input("Digita esponente secondo numero : "))
ax = NumeroComplesso(a, x)
by = NumeroComplesso(b, y)

# TODO: arrotondamento

print("Forma Algebrica ax : " + ax.getNumeroComplesso())
print("Forma Algebrica by : " + by.getNumeroComplesso() + "\n")

print("Forma Trigonometrica ax : " + ax.getFormaTrigonometrica())
print("Forma Trigonometrica by : " + by.getFormaTrigonometrica() + "\n")

print("coniugato ax : " + ax.getConiugato().getNumeroComplesso())
print("coniugato by : " + by.getConiugato().getNumeroComplesso() + "\n")

print("modulo ax : " + str(ax.getModulo()))
print("modulo by : " + str(by.getModulo()) + "\n")

print("Somma : " + oanc.sommaComplessa(ax=ax, by=by).getNumeroComplesso() + "\n")

print("differenza ax - by : " + oanc.differenzaComplessa(ax=ax, by=by).getNumeroComplesso())
print("differenza by - ax : " + oanc.differenzaComplessa(ax=by, by=ax).getNumeroComplesso() + "\n")

print("prodotto : " + oanc.prodottoComplesso(ax=ax, by=by).getNumeroComplesso() + "\n")
print("prodotto trigonometrica" + otnc.prodottoTrigonometrico(ax=ax, by=by).getFormaTrigonometrica())

print("quoziente ax/by : " + oanc.quozienteComplesso(ax=ax, by=by).getNumeroComplesso())
print("quoziente trigonometrica ax/by : " + otnc.quozienteTrigonometrico(ax=ax, by=by).getFormaTrigonometrica())
print("quoziente by/ax : " + oanc.quozienteComplesso(ax=by, by=ax).getNumeroComplesso())
print("prodotto trigonometrica by/ax :" + otnc.quozienteTrigonometrico(ax=by, by=ax).getFormaTrigonometrica())

print("elevamento ax a " + str(eax) + otnc.elevamentoTrigonmetrico(ax=ax, e=eax).getNumeroComplesso())
print("elevamento by a " + str(eby) + otnc.elevamentoTrigonmetrico(ax=by, e=eby).getNumeroComplesso())

