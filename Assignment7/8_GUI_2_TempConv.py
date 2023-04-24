from tkinter import Tk, StringVar, Label, Entry, Button, mainloop, W, DoubleVar
from datetime import date
def fahrToCels():
    celsius = (fahrenVar.get() - 32) * 5 / 9
    celsiusVar.set(celsius)

def celsToFahr():
    fahren = (celsiusVar.get() * 9 / 5) + 32
    fahrenVar.set(fahren)
    
master=Tk()
fahrenVar = DoubleVar()
celsiusVar = DoubleVar()
fahrenVar.set(32.0)
celsiusVar.set(0)

Label(master, text="Fahrenheit").grid(row=0, column=1, pady=5)
Label(master, text="Celsius").grid(row=0, column=2, pady=5)
fahrenEntry = Entry(master, textvariable=fahrenVar).grid(row=1, column=1, padx=5)
celsiusEntry = Entry(master, textvariable=celsiusVar).grid(row=1, column=2, padx=5)

areaButton = Button(master, text=">>>>>>", command=fahrToCels)
areaButton.grid(row=2, column=1, pady=5)
areaButton = Button(master, text="<<<<<<", command=celsToFahr)
areaButton.grid(row=2, column=2, pady=5)

mainloop()