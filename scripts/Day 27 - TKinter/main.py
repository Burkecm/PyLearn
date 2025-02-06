from tkinter import *

def convert_mi_to_km(miles):
    if miles == "":
        return 0
    return str(float(miles) * 1.6)

def button_clicked():
    label_output.config(text=convert_mi_to_km(input_miles.get()))

window = Tk()
window.title("Miles to KM Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

input_miles = Entry(text="test", width=5)
label_miles = Label(text="Miles", justify="left")
label_desc = Label(text="is equal to")
label_output = Label(text="0")
label_km = Label(text="Km") #f"is equal to {convert_units(input_miles.get())}"
button_calc = Button(text="Calculate",command=button_clicked)

input_miles.grid(column=1, row=0)
label_miles.grid(column=3, row=0)
label_desc.grid(column=0, row=1)
label_km.grid(column=2, row=1)
label_output.grid(column=1, row=1)
button_calc.grid(column=1, row=3)
window.mainloop()