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
window.config(padx=50, pady=50, bg=YELLOW)

def start_timer():
    print("Start clicked")

def reset_click():
    print("Reset clicked")

# canvas widget
canvas = Canvas(width=300, height=400, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(200, 212, image=tomato_img)
canvas.create_text(205, 220, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
#canvas.pack()
canvas.grid()

timer_label = Label(text="Timer", font=("Arial", 40))
timer_label.config(fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

button_start = Button(text="Start", command=start_timer)
#button_start.pack(side="left")
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_click)
#button_reset.pack(side="right")
button_reset.grid(column=2, row=2)

checkmark_label = Label(text=checkmark, font=("Arial", 20))
checkmark_label.config(fg=GREEN, bg=YELLOW)
#checkmark_label.pack(side="bottom")
checkmark_label.grid(column=0, row=3)

window.mainloop()