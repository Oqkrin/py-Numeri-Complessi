import tkinter as tk

root = tk.Tk()
root.title("Differenza")

label1 = tk.Label(root, text="primo numero: ")
label2 = tk.Label(root, text="secondo numero: ")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

def CalcDiff():
    a = int(input(entry1.get()))
    b = int(input(entry2.get()))
    if a > b:
        ris = a - b
        Label_ris = tk.Label(root, text="la differenza è: " + f"{ris}")
        Label_ris.grid(row=2, column=1)
    else:
        ris = b-a
        Label_ris = tk.Label(root, text="la differenza è: " + f"{ris}")
        Label_ris.grid(row=2, column=1)


button = tk.Button(root, text="Calcola", command=CalcDiff)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
button.grid(row=2, column=1)

root.mainloop()
