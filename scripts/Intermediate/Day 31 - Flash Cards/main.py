from tkinter import *
from pandas import *
import random as rand
BACKGROUND_COLOR = "#B1DDC6"
IMG_CARD_FRONT = "scripts\\Intermediate\\Day 31 - Flash Cards\\images\\card_front.png"
IMG_CARD_BACK = "C:\\Users\\burkec\\source\\repos\\PyLearn\\scripts\\Intermediate\\Day 31 - Flash Cards\\images\\card_back.png"
IMG_CHECKMARK = "C:\\Users\\burkec\\source\\repos\\PyLearn\\scripts\\Intermediate\\Day 31 - Flash Cards\\images\\right.png"
IMG_X = "C:\\Users\\burkec\\source\\repos\\PyLearn\\scripts\\Intermediate\\Day 31 - Flash Cards\\images\\wrong.png"
WORD_FILEPATH = "scripts\\Intermediate\\Day 31 - Flash Cards\\data\\words_to_learn.csv"

def next_card():
    global current_card, flip_timer
    current_card = rand.choice(words_to_learn)
    canv.itemconfig(card_title, text="French", fill="black")
    canv.itemconfig(card_word, text=current_card["French"], fill="black")
    canv.itemconfig(canv_img, image=img_card_front)
    win.after_cancel(flip_timer)
    flip_timer = win.after(3000, func=flip_card)

def flip_card():
    global current_card
    canv.itemconfig(card_title, text="English", fill="white")
    canv.itemconfig(card_word, text=current_card["English"], fill="white")
    canv.itemconfig(canv_img, image=img_card_back)

def is_known():
    global current_card
    words_to_learn.remove(current_card)
    DataFrame(words_to_learn).to_csv(WORD_FILEPATH, index=False)
    next_card()

try:
    words_to_learn = read_csv(WORD_FILEPATH).to_dict(orient="records")
except FileNotFoundError:
     words_to_learn = read_csv("scripts\\Intermediate\\Day 31 - Flash Cards\\data\\french_words.csv").to_dict(orient="records")

current_card = {}
win = Tk()
win.title("Flashy")
win.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

img_card_front = PhotoImage(file=IMG_CARD_FRONT)
img_card_back = PhotoImage(file=IMG_CARD_BACK)
img_checkmark = PhotoImage(file=IMG_CHECKMARK)
img_x = PhotoImage(file=IMG_X)
flip_timer = win.after(3000, func=flip_card)

canv = Canvas(width=800, height=526, highlightthickness=0)
canv_img = canv.create_image(400, 263, image=img_card_front)
card_title = canv.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canv.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canv.config(background=BACKGROUND_COLOR)
canv.grid(column=0, row=0, columnspan=2)


btn_known = Button(image=img_checkmark, highlightthickness=0, command=is_known)
btn_known.grid(column=1, row=1)

btn_unknown = Button(image=img_x, highlightthickness=0, command=next_card)
btn_unknown.grid(column=0, row=1)

next_card()

win.mainloop()