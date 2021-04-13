# Bibliothek importieren
from tkinter import *
from tkinter import messagebox
import tkinter

# Ein Fenster bauen
Fenster = Tk()

# ===================================Einstellungen==========================================

# die Länge und Breite des Fensters festsetzen
Fenster.geometry("313x245")
# Fenstergrösse beschränken
Fenster.resizable(width=False, height=False)
# Titel zum Fenster hinzufügen
Fenster.title('Rechner')


# ===================================Funktionen==========================================

Operator = ""

# Funktion zur Anzeige von Fehlern


def errorMsg(ms):
    if ms == 'Error':
        tkinter.messagebox.showerror('Error', 'Irgenwas stimmt nicht')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror(
            'Division Error', 'Kann nicht durch Null geteilt werden')


# Funktion zum klicken auf den Tasten
def btn_klick(Nummern):
    try:
        global Operator
        Operator += str(Nummern)
        derText_desEingangs.set(Operator)
    except:
        errorMsg('Error')


# Funktion zum löschen
def btn_loschen():
    try:
        global Operator
        Operator = " "
        derText_desEingangs.set(Operator)
    except:
        errorMsg('Error')


# Tastenfunktionen +-*/
def btn_kalkulieren(Symbole):
    try:
        global Operator
        Operator += str(Symbole)
        derText_desEingangs.set(Operator)
    except:
        errorMsg('Error')


# Funktion zur die Taste von Gleichheitszeichen
def btn_gleichheitszeichen():
    try:
        global Operator
        erhalten_Texte = derText_desEingangs.get()
        Str_erhalten_Texte = str(erhalten_Texte)
        Ergebnis = str(eval(Str_erhalten_Texte))
        btn_loschen()
        derText_desEingangs.set(Ergebnis)
    except:
        errorMsg('Error')


# =======================================Tasten==============================================

# String fassen
derText_desEingangs = StringVar()

# die Eingabe,um Informationen zu erhalten und das Ergebnis anzeigen
Eintrag_1 = Entry(Fenster, width=30, font=('arial', 10, 'bold'),
                  bd=8, insertwidth=4, bg='powder blue', textvariable=derText_desEingangs)
Eintrag_1.grid(row=5, column=0, rowspan=1, columnspan=3)


# Funktion für die Tasten erstellen
def button(Text, Reihe, Pfeiler, Breite=10, height=3, rowspan=1, columnspan=1, command=None):
    Knopf = Button(master=Fenster, text=Text,
                   highlightbackground="gray", padx=3, pady=3, bd=4, fg='black', font=('arial', 7, 'bold'), width=Breite, height=height, command=command)
    Knopf.grid(row=Reihe, column=Pfeiler,
               rowspan=rowspan, columnspan=columnspan)
    return Knopf


# Taste Nummer sieben
button("7", 7, 0, command=lambda: btn_klick(7))

# Taste Nummer acht
button("8", 7, 1, command=lambda: btn_klick(8))

# Taste Nummer neun
button("9", 7, 2, command=lambda: btn_klick(9))

# Taste Nummer vier
button("4", 8, 0, command=lambda: btn_klick(4))

# Taste Nummer fünf
button("5", 8, 1, command=lambda: btn_klick(5))

# Taste Nummer sechs
button("6", 8, 2, command=lambda: btn_klick(6))

# Taste Nummer eins
button("1", 9, 0, command=lambda: btn_klick(1))

# Taste Nummer zwei
button("2", 9, 1, command=lambda: btn_klick(2))

# Taste Nummer drei
button("3", 9, 2, command=lambda: btn_klick(3))

# Taste plus
button("+", 7, 3, command=lambda: btn_kalkulieren("+"))

# Taste minus
button("-", 8, 3, command=lambda: btn_kalkulieren("-"))

# Taste mal
button("*", 9, 3, command=lambda: btn_kalkulieren("*"))

# Taste durch
button("/", 10, 3, command=lambda: btn_kalkulieren("/"))

# Taste null
button("0", 10, 0, columnspan=1, command=lambda: btn_klick(0))

# Taste löschen
button("C", 5, 3, command=lambda: btn_loschen())

# Taste Punkt
button(".", 10, 1, command=lambda: btn_kalkulieren("."))

# Taste Gleichung
button("=", 10, 2, command=lambda: btn_gleichheitszeichen())


# ein Loop für das Programm erstellen
Fenster.mainloop()
