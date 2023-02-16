import tkinter as tk
from NumeroComplesso import NumeroComplesso as z
import OperazioniTrigonometricheNC as otnc
import OperazioniAlgebricheNC as oanc

class interfaccia:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Circosta and Ionà project")
        self.root.iconbitmap("Logo.ico")

        self.sceltaIniziale()

        self.root.mainloop()

    def sceltaIniziale(self):
        self.option = ["Trigonometrica", "Aritmetica"]
        variable = tk.StringVar(self.root)
        variable.set(self.option[0])

        scelta = tk.OptionMenu(self.root, variable, *self.option)
        scelta.grid(row=0, column=0)

        start = tk.Button(self.root, text="Start", command=lambda: self.operazioni())
        start.grid(row=0, column=1)

    def operazioni(self):
        if self.option == self.option[0]:
            print("abc")
            self.trigonometrica()
        else:
            self.algebrica()

    def trigonometrica(self):
        label1 = tk.Label(self.root, text="angoli in: ")
        label1.grid(row=1, column=0)

        option = ["Radianti", "Gradi"]
        variable = tk.StringVar(self.root)
        variable.set(option[0])

        scelta = tk.OptionMenu(self.root, variable, *option)
        scelta.grid(row=1, column=1)

    def algebrica(self):
        pass


