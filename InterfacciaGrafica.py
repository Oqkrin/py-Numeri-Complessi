import tkinter as tk
import customtkinter as ctk
from NumeroComplesso import NumeroComplesso as z
import OperazioniTrigonometricheNC as otnc
import OperazioniAlgebricheNC as oanc


class Interfaccia:

    def __init__(self):

        self.contatoreRighe = -1  # -1 perchè vengono incrementate alla prima chiamata della funzione
        self.contatoreColonne = -1  # -1 perchè vengono incrementate alla prima chiamata della funzione
        self.contatoreAssoluto = 0

        self.root = tk.Tk()
        self.root.title("Circosta and Ionà project")
        self.root.iconbitmap("Logo.ico")

        self.pulsanteDiControllo = tk.Button(self.root, text="ᐉ")
        self.modoInserimentoNC = tk.StringVar(self.root)
        self.modoInserimentoAngolo = tk.StringVar(self.root)

        self.SceltaModoInserimentoNC()

        self.root.mainloop()

    def controlloModoInserimentoNc(self):
        match self.modoInserimentoNC.get():
            case "Trigonometrica":
                self.inputTrigonometrico()
            case "Algebrica":
                self.inputAlgebrico()

    def controlloModoInserimentoAngolo(self):
        match self.modoInserimentoAngolo.get():
            case "Gradi":
                self.campoInputNumeroComplesso(usaCoordinatePolari=True, usaRadianti=False)
            case "Radianti":
                self.campoInputNumeroComplesso(usaCoordinatePolari=True, usaRadianti=True)

    def SceltaModoInserimentoNC(self):

        self.contatoreRighe += 1
        self.modoInserimentoNC.set("Modalità Input Numero Complesso")
        sceltaModoInserimentoNC = tk.OptionMenu(self.root, self.modoInserimentoNC,
                                                *["Trigonometrica", "Algebrica"])
        sceltaModoInserimentoNC.grid(row=self.contatoreRighe, column=0)

        self.pulsanteDiControllo.config(command=lambda: self.controlloModoInserimentoNc())
        self.pulsanteDiControllo.grid(row=self.contatoreRighe, column=1)

    def inputTrigonometrico(self):
        self.contatoreRighe += 1

        self.modoInserimentoAngolo.set("Modalità Input Angolo")
        sceltaModoInserimentoAngolo = tk.OptionMenu(self.root, self.modoInserimentoAngolo,
                                                    *["Gradi", "Radianti"])
        sceltaModoInserimentoAngolo.grid(row=self.contatoreRighe, column=0)
        self.pulsanteDiControllo.config(command=lambda: self.controlloModoInserimentoAngolo())
        self.contatoreAssoluto += 1
        self.pulsanteDiControllo.grid(row=self.contatoreRighe, column=1)

    def inputAlgebrico(self):
        self.contatoreRighe += 1
        self.contatoreAssoluto += 1
        self.campoInputNumeroComplesso()

    def campoInputNumeroComplesso(self, usaCoordinatePolari=False, usaRadianti=False):
        self.contatoreAssoluto += 1
        self.contatoreRighe += 1
        r = tk.Entry(self.root)
        ia = tk.Entry(self.root)
        r.grid(row=self.contatoreRighe, column=0)
        ia.grid(row=self.contatoreRighe, column=1)
        self.pulsanteDiControllo.config(
            command=lambda: self.mostraRis(r=r, ia=ia, usaCoordinatePolari=usaCoordinatePolari,
                                           usaRadianti=usaRadianti))
        self.contatoreAssoluto += 1
        self.pulsanteDiControllo.grid(row=self.contatoreRighe, column=2)

    def mostraRis(self, r, ia, usaCoordinatePolari, usaRadianti):
        self.contatoreAssoluto += 1
        nc = z(r=r.get() if r.get() != "" else 0, ia=ia.get() if ia.get() != "" else 0, usaRadianti=usaRadianti,
               usaCoordinatePolari=usaCoordinatePolari)
        labelRis = tk.Label(text="= " + nc.getFormTrigonometrica() if usaCoordinatePolari else nc.getFormAlgebrica())
        labelRis.grid(row=self.contatoreRighe, column=3)
        self.SceltaModoInserimentoNC()


class ctkInterfaccia(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.toplevel_window = None
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        self.stato = False
        larghezza = 426
        altezza = 300
        x = 100
        y = 100

        self.title("Calcolatrice Numeri complessi by Circosta e Ionà")
        self.iconbitmap("Logo.ico")
        self.minsize(larghezza, altezza)
        self.geometry("{w}x{h}+{x}+{y}".format(w=larghezza, h=altezza, x=x, y=y))


