from tkinter import *
from tkinter import messagebox
from password import Password
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = Password(8, 4, 2).generate()
    entry_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
filepath = "scripts\\Day 29 - Password Manager\\passwords.csv"
def save():
    site = entry_site.get()
    user = entry_user.get()
    pwd = entry_pass.get()
    if len(site) == 0 or len(user) ==0 or len(pwd) == 0:
        messagebox.showerror(title="You Forgot something!", message="Please do not leave any fields blank.")
        return
    confirm_message = f"Site: {site} \nUser: {user} \nPassword: {pwd}"
    if messagebox.askokcancel(title="Are you sure?", message=f"Add the following set of credentials? \n{confirm_message}") == False:
        return 
    with open(filepath, mode="a") as file:
        file.write(f"\"{site}\", \"{user}\", \"{pwd}\"\n")
        entry_site.delete(0, END)
        # entry_user.delete(0, END)
        entry_pass.delete(0, END)
        entry_site.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width=400, height=400, padx=50, pady=50, bg="white")
window.minsize(width=300, height=300)
canv = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="scripts\\Day 29 - Password Manager\\logo.png")
canv.create_image(100, 100, image=img)
canv.grid(column=1, row=0)

# Labels
label_site = Label(text="Site:", bg="white")
label_user = Label(text="Email/Username:", bg="white")
label_pass = Label(text="Password:", bg="white")

# Buttons
btn_generate_pass = Button(text="Generate Password", justify="left", bg="white", command=generate_password)
btn_add = Button(text="Add", bg="white", width=42, command=save)


# Entries
entry_site =Entry(bg="white", width=50)
entry_user = Entry(bg="white", width=50)
entry_pass = Entry(bg="white", width=32)

# Layout
label_site.grid(column=0, row=1, sticky="e")
entry_site.grid(column=1, row=1, columnspan=2)
entry_site.focus()

label_user.grid(column=0, row=2, sticky="e")
entry_user.grid(column=1, row=2, columnspan=2)

label_pass.grid(column=0, row=3, sticky="e")
entry_pass.grid(column=1, row=3)
btn_generate_pass.grid(column=2, row=3)

btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()