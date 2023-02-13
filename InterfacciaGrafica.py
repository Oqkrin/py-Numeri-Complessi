import tkinter as tk


def operazioni():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    ris = 0
    if variable.get() == option[0]:
        ris = num1 + num2
    elif variable.get() == option[1]:
        ris = num1 - num2
    elif variable.get() == option[2]:
        ris = num1 * num2
    elif variable.get() == option[3]:
        ris = num1 / num2

    risultato = str(ris)
    labelRis.config(text="ris: " + risultato)

root = tk.Tk()
root.iconbitmap("Logo.ico")
root.title("numeri complessi by Circosta e Ionà")
root.overrideredirect(False)

label1 = tk.Label(root, text="primo numero")
label2 = tk.Label(root, text="secondo numero")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

label1.grid(row=0, column=0)
label2.grid(row=0, column=2)

entry1.grid(row=1, column=0)
entry2.grid(row=1, column=2)


option = ["Somma", "Differenza", "Prodotto", "Quoziente"]
variable = tk.StringVar(root)
variable.set(option[0])

scelta = tk.OptionMenu(root, variable, *option)
scelta.grid(row=1, column=1)

button = tk.Button(root, text="Calcola risultato", command=operazioni)
button.grid(row=2, column=0)

labelRis = tk.Label(root)
labelRis.grid(row=2, column=1)
root.mainloop()