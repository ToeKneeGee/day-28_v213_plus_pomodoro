from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checkmark = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=20, pady=20, bg=YELLOW)

def start_timer():
    print("Start clicked")

def reset_click():
    print("Start clicked")
# canvas widget
canvas = Canvas(width=300, height=500, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(175, 280, image=tomato_img)
canvas.create_text(180, 300, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
#canvas.pack()
canvas.grid()

timer_label = Label(text="Timer", font=("Arial", 40))
timer_label.config(fg=GREEN, bg=YELLOW)
timer_label.grid(column=0, row=0)
#timer_label.grid()

button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=1)

checkmark_label = Label(text="check", font=("Arial", 40))
checkmark_label.grid(column=0, row=1)

button_reset = Button(text="Reset", command=reset_click())
button_reset .grid(column=2, row=1)

window.mainloop()