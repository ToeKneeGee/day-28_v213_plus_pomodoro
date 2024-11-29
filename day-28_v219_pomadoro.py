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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    print("18- Reset clicked")
    # stop the timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    #print("Start clicked")
    global reps
    global checkmark
    reps += 1
    print(f"23- reps: {reps} <---------------------------------------------")
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # the count_down function requires canvas so it must be after the canvas widget
    count_down(5 * 60)

    # 25min work
    #   5min short break
    # 25min work
    #   5min short break
    # 25min work
    #   5min short break
    # 25min work
    #               20m long break

    # if it's the 8th rep:
    if reps % 8 == 0:
        # print(f"44- RED, long_break_sec ================: {long_break_sec}")
        # set_timer_label("Long Break", RED)
        title_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    # if it's the 2nd/4th/6th/rep:
    elif reps % 2 == 0:
        # print(f"50- PINK, short_break_sec ================: {short_break_sec}")
        # set_timer_label("Short Break", PINK)
        title_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    # if it's the 1st/3rd/5th/7th rep:
    else:
        print(f"53- GREEN, work_sec: {work_sec} checkmark: {checkmark}")
        # set_timer_label("Work", GREEN)
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    "01:35"
    #print(f"63- count: {count}")
    minutes = math.floor(count / 60)
    seconds = count % 60
    #print(f"66- seconds: {seconds}, {type(seconds)}")

    if minutes == 0:
        minutes = "00"
    elif minutes < 10:
        minutes = f"0{minutes}"

    if seconds == 0:
        seconds = "00"
    elif seconds <  10:
        seconds = f"0{seconds}"

    # the canvas.itemconfig allows us to use the timer to count down on the GUI
    #print(f"79- minutes: {minutes}")
    #print(f"80- seconds: {seconds}, {type(seconds)}")
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 60))
title_label.config(fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# canvas widget
canvas = Canvas(width=410, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(220, 145, image=tomato_img)
timer_text = canvas.create_text(230, 160, text="00:00", fill="white", font=(FONT_NAME,40, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

#checkmark_label = Label(text=checkmark, font=("Arial", 25))
checkmark_label = Label(font=("Arial", 20))
checkmark_label.config(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()