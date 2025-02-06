# funcs with any num of arguments (*args)
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
print(add(1, 2, 3, 45))

# funcs with any num of key word arguments (**kwargs)
def calc(n, **kwargs):
    n+= kwargs["add"]
    n *= kwargs["mult"]
    print(n)
calc(2, add=3, mult = 5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

    def print_car(self):
        print(f"You bought a {self.make} {self.model}!")
my_car = Car(make="Subaru")#, model="Legacy")
my_car.print_car()


# GUIs via TKinter
from tkinter import *
window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Labels 
label = Label(text="I am a Label!", font=("Arial", 24, "bold"))
# label.pack()
label["text"] = "Still a label"
label.config(text="Three times a label")

# Buttons
def button_clicked():
    label.config(text=input_field.get())
    # label.config(text="He touched the butt!")
    print("He touched the butt!")
button = Button(text="Click Me", command=button_clicked)
# button.pack()

# Entry Fields
input_field = Entry()
# input_field.pack()
# input_field.get()

# Layout Managers: pack(), place(), grid()
# label.place(x=100, y=200) # Takes exact coords
# button.grid(column=0, row=0) # Takes indexed coords. Cannot mix and match with pack()
label.grid(column=0, row=0)
button.grid(column=1, row=1)
input_field.grid(column=3, row=2)
button2 = Button(text="New Button")
button2.grid(column=2, row=0)

window.mainloop()