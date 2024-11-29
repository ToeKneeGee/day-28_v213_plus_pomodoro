from tkinter import *
import math
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
def start_timer():
    print("Start clicked")
    # the count_down function requires canvas so it must be after the canvas widget
    count_down(5 * 60)
    #count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    "01:35"
    #count = count * 60
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"

    # the canvas.itemconfig allows us to use the timer to count down on the GUI
    #new_count = str(minutes) + ":" + str(seconds)
    print(f"31- count: {count}")
    print(f"32- minutes: {minutes}")
    print(f"33- seconds: {seconds}")
    #print(f"31- new_count: {new_count}")
    #canvas.itemconfig(timer_text, text=count)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        # print(f"38- count: {count}")
        # count -= 1
        # print(f"40- count: {count}")
        window.after(1000, count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
#window.config(padx=50, pady=50, bg=YELLOW)
#window.config(padx=30, pady=30, bg=YELLOW)
window.config(padx=10, pady=50, bg=YELLOW)


def reset_click():
    print("Reset clicked")

timer_label = Label(text="Timer", font=(FONT_NAME, 60))
timer_label.config(fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# canvas widget
#canvas = Canvas(width=300, height=400, bg=YELLOW, highlightthickness=0)
#canvas = Canvas(width=300, height=400, bg=YELLOW, highlightthickness=0)
#canvas = Canvas(width=350, height=300, bg=YELLOW, highlightthickness=0)
canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
#canvas.create_image(200, 212, image=tomato_img)
canvas.create_image(140, 145, image=tomato_img)
timer_text = canvas.create_text(150, 160, text="00:00", fill="white", font=(FONT_NAME,40, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_click)
button_reset.grid(column=2, row=2)

checkmark_label = Label(text=checkmark, font=("Arial", 25))
checkmark_label.config(fg=GREEN, bg=YELLOW)
#checkmark_label.pack(side="bottom")
checkmark_label.grid(column=1, row=3)

window.mainloop()