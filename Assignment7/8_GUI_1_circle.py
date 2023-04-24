from tkinter import Tk, StringVar, Label, Entry, Button, mainloop, W, DoubleVar
from datetime import date
def calcArea():
    areaVar.set(f"Area = {3.14*radiusVar.get()**2:.2f}")

def calcCircumference():
    circumVar.set(f"Circumference = {2*3.14*radiusVar.get():.2f}")
    
master=Tk()
radiusVar = DoubleVar()
areaVar = StringVar()
circumVar = StringVar()

Label(master, text="Radius").grid(row=0)
radiusEntry = Entry(master, textvariable=radiusVar).grid(row=0, column=1)

areaButton = Button(master, text="Calculate Area", command=calcArea)
areaButton.grid(row=1, column=0)
areaLabel = Label(master, textvariable=areaVar ).grid(row=1, column=1)

circumButton = Button(master, text="Calculate Circumferecne", command=calcCircumference)
circumButton.grid(row=2, column=0)
circumLabel = Label(master, textvariable=circumVar ).grid(row=2, column=1)

mainloop()