from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    completed_pomos.config(text="")
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        label.config(text="Break!", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        label.config(text="Break!", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        label.config(text="Work!", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    canvas.itemconfig(timer_text, text=format_time(count))
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        checks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            checks += "✓"
        completed_pomos.config(text=checks)

def format_time(count):
    mins = math.floor(count / 60)
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"
    return f"{mins}:{secs}"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Mangia la Pomodoro!")
window.minsize(height=300, width=300)
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas Setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="scripts\\Day 28 - Pomodoro\\tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", bg=YELLOW,  fg=GREEN, font=(FONT_NAME, 36, "bold"))
label.grid(column=1, row=0)
# countdown(5)
# Pomo Tracker: ✓
completed_pomos = Label(text="", bg=YELLOW,  fg=GREEN, font=(FONT_NAME, 24, "bold"))
completed_pomos.grid(column=1, row=3)

# Buttons
button_start_timer = Button(text="Start", command=start_timer)
button_start_timer.grid(column=0, row=2)
button_reset_timer = Button(text="Reset", command=reset_timer)
button_reset_timer.grid(column=2, row=2)
window.mainloop()