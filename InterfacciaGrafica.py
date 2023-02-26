import threading
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


def appendToN(lista, n):
    while len(lista) != n + 1:
        lista.append(lista[0])
    return lista


class ctkInterfaccia(ctk.CTk):
    def __init__(self):
        super().__init__()

        # attributi
        self.contatoreRighe = 0
        self.risLabelAlgebrico = []
        self.parteReale = []
        self.parteImmaginaria = []
        larghezza = 426
        altezza = 300
        x = 100
        y = 100
        self.inputAlgebrico = None
        self.ris = [z()]

        # stile base
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        # propietà base
        self.title("Calcolatrice Numeri complessi by Circosta e Ionà")
        self.iconbitmap("Logo.ico")
        self.minsize(larghezza, altezza)
        self.geometry(f"{larghezza}x{altezza}+{x}+{y}")

        # configurazione griglia
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # configurazione modalità display numeri complessi
        self.tabsTipiNC = ctk.CTkTabview(self)
        self.tabsTipiNC.grid(row=1, column=1)

        self.algebrica = self.tabsTipiNC.add("Algebrica")
        self.ConfiguraModalitaAlgebrica(32)
        self.ConfiguraModalitaTrigonometrica()
        self.ConfiguraModalitaEsponenziale()

    def ConfiguraModalitaAlgebrica(self, value):
        i = self.contatoreRighe
        self.contatoreRighe += 1

        def aggiornaCampoAlgebrico():
            for j in range(0, i + 1):
                try:
                    self.parteReale[j].get()
                    self.parteImmaginaria[j].get()
                except IndexError:
                    self.parteReale.append(idEntry(master=None, numericIdentifier=j))
                    self.parteImmaginaria.append(idEntry(master=None, numericIdentifier=j))
                if len(self.ris) == j:
                    self.ris.append(z())
                else:
                    self.ris[j] = z(r=self.parteReale[j].get(), ia=self.parteImmaginaria[j].get())

                self.risLabelAlgebrico[j].configure(text="= " + self.ris[j].getFormAlgebrica())
                self.risLabelAlgebrico[j].grid(row=j, column=3)
            return True

        if i == 0:
            self.risLabelAlgebrico.append(ctk.CTkLabel(master=self.algebrica, text="= 0"))
        else:
            self.risLabelAlgebrico = appendToN(self.risLabelAlgebrico, i)

        self.risLabelAlgebrico[i].grid(row=i, column=3)

        if i == 0:
            self.parteReale.append(idEntry(master=None, numericIdentifier=i))
        else:
            self.parteReale = appendToN(self.parteReale, i)

        self.parteReale[i] = idEntry(master=self.algebrica,
                                     numericIdentifier=i,
                                     placeholder_text="Parte Reale",
                                     validate="all",
                                     validatecommand=(self.register(aggiornaCampoAlgebrico)))
        self.parteReale[i].grid(row=i, column=0)

        if i == 0:
            self.parteImmaginaria.append(idEntry(master=None, numericIdentifier=i))
        else:
            self.parteImmaginaria = appendToN(self.parteImmaginaria, i)
        self.parteImmaginaria[i] = idEntry(master=self.algebrica,
                                           numericIdentifier=i,
                                           placeholder_text="Parte Immaginaria",
                                           validate="all",
                                           validatecommand=(self.register(aggiornaCampoAlgebrico)))
        self.parteImmaginaria[i].grid(row=i, column=1)
        self.operazioneDaConcatenareAlgebrica()

    def operazioneDaConcatenareAlgebrica(self):
        self.contatoreRighe += 1
        menuOperazioni = ctk.CTkOptionMenu(master=self.algebrica, values=["+", "-", "*", "/", "="],
                                           variable=ctk.StringVar(value="Scegli Operazione"),
                                           command=self.ConfiguraModalitaAlgebrica)
        menuOperazioni.grid(row=self.contatoreRighe, column=1)

    def ConfiguraModalitaTrigonometrica(self):
        trigonometrica = self.tabsTipiNC.add("Trigonometrica")
        modulo = ctk.CTkEntry(master=trigonometrica, placeholder_text="Modulo")
        modulo.grid(row=0, column=0)
        angolo = ctk.CTkEntry(master=trigonometrica, placeholder_text="Angolo")
        angolo.grid(row=0, column=1)
        self.inputTrigonometrico = None

    def ConfiguraModalitaEsponenziale(self):
        esponenziale = self.tabsTipiNC.add("Esponenziale")
        # configurazione griglia per esponenziali
        esponenziale.grid_rowconfigure(0, weight=1)
        esponenziale.grid_rowconfigure(1, weight=1)
        esponenziale.grid_rowconfigure(2, weight=1)
        esponenziale.grid_columnconfigure(0, weight=1)
        esponenziale.grid_columnconfigure(1, weight=1)
        esponenziale.grid_columnconfigure(2, weight=1)
        # testo centrato
        labelEsponenzialeWIP = ctk.CTkLabel(master=esponenziale, text="Work in Progress")
        labelEsponenzialeWIP.grid(row=1, column=1)


class idEntry(ctk.CTkEntry):
    def __init__(self, master: any, numericIdentifier: int, **kwargs):
        super().__init__(master, **kwargs)
        self.id = numericIdentifier
