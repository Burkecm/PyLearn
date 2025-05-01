from tkinter import *
from tkinter import messagebox
from password import Password
import pyperclip
import json

FILEPATH = "scripts\\Intermediate\\Day 30 - Exceptions\\passwords.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = Password(8, 4, 2).generate()
    entry_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = entry_site.get()
    user = entry_user.get()
    pwd = entry_pass.get()
    if len(site) == 0 or len(pwd) == 0:
        messagebox.showerror(title="You Forgot something!", message="Please do not leave any fields blank.")
        return
    confirm_message = f"Site: {site} \nUser: {user} \nPassword: {pwd}"
    if messagebox.askokcancel(title="Are you sure?", message=f"Add the following set of credentials? \n{confirm_message}") == False:
        return 
    
    new_credential = {
        site: {
            "email": user,
            "password": pwd,
        }
    }
    try:
        with open(FILEPATH, mode="r") as file:
            all_credentials = json.load(file)
    except FileNotFoundError as file_error:
        print(f"File Not Found: {file_error}")
        with open(FILEPATH, mode="w") as file:
            json.dump(new_credential, file, indent=4)
    except json.JSONDecodeError as json_error:
        print(f"json decoder error: {json_error}")
        with open(FILEPATH, mode="w") as file:
            json.dump(new_credential, file, indent=4)
    else:
        all_credentials.update(new_credential)
        with open(FILEPATH, mode="w") as file:
            json.dump(all_credentials, file, indent=4)
            entry_site.delete(0, END)
            entry_pass.delete(0, END)
            entry_site.focus()
# ---------------------------- Password Search ------------------------------- #
def search():
    cred_to_find = entry_site.get()
    try: 
        with open(FILEPATH, "r") as file:
            all_sites = json.load(file)
        cred = all_sites[cred_to_find]
    except FileNotFoundError as fnf:
        messagebox.showwarning(title="File not Found", message=fnf)
    except KeyError as key:
        print(f"Key {key} not found.")
    else:
        messagebox.showinfo(message=f"Email: {all_sites[cred_to_find]["email"]} \nPassword: {all_sites[cred_to_find]["password"]}")
        print((f"Email: {all_sites[cred_to_find]["email"]} \nPassword: {all_sites[cred_to_find]["password"]}"))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width=400, height=400, padx=50, pady=50, bg="white")
window.minsize(width=300, height=300)
canv = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="scripts\\Intermediate\\Day 30 - Exceptions\\logo.png")
canv.create_image(100, 100, image=img)
canv.grid(column=1, row=0)

# Labels
label_site = Label(text="Site:", bg="white")
label_user = Label(text="Email/Username:", bg="white")
label_pass = Label(text="Password:", bg="white")

# Buttons
btn_generate_pass = Button(text="Generate Password", justify="left", bg="white", command=generate_password)
btn_add = Button(text="Add", bg="white", width=42, command=save)
btn_search = Button(text="Search", bg="white", command=search)


# Entries
entry_site =Entry(bg="white", width=32)
entry_user = Entry(bg="white", width=50)
entry_user.insert(0, "burkecm77@gmail.com")
entry_pass = Entry(bg="white", width=32)

# Layout
label_site.grid(column=0, row=1, sticky="e")
entry_site.grid(column=1, row=1)
btn_search.grid(column=2, row=1)
entry_site.focus()

label_user.grid(column=0, row=2, sticky="e")
entry_user.grid(column=1, row=2, columnspan=2)

label_pass.grid(column=0, row=3, sticky="e")
entry_pass.grid(column=1, row=3)
btn_generate_pass.grid(column=2, row=3)

btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
