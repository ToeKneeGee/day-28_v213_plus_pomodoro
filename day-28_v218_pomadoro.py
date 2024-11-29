from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 # defult 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checkmark = "✔"
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    print("Start clicked")
    global reps
    reps += 1
    print(f"22- reps: {reps} <---------------------------------------------")
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # the count_down function requires canvas so it must be after the canvas widget
    count_down(5 * 60)
    #count_down(WORK_MIN * 60)

    #if count == (25 * 60) and

    # 25min work
    #   5min short break
    # 25min work
    #   5min short break
    # 25min work
    #   5min short break
    # 25min work
    #               20m long break

    # if it's the 8th rep:
    #elif reps == 8:
    if reps % 8 == 0:
        # print(f"44- RED, long_break_sec ================: {long_break_sec}")
        # set_timer_label("Long Break", RED)
        title_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    # if it's the 2nd/4th/6th/rep:
    #elif reps == 2 or reps == 4 or reps == 6:
    elif reps % 2 == 0:
        # print(f"50- PINK, short_break_sec ================: {short_break_sec}")
        # set_timer_label("Short Break", PINK)
        title_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    # if it's the 1st/3rd/5th/7th rep:
    # if reps == 1 or reps == 3 or reps == 5 or reps == 7:
    else:
        # print(f"56- GREEN, work_sec ================: {work_sec}")
        # set_timer_label("Work", GREEN)
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    "01:35"
    print(f"63- count: {count}")
    #count = count * 60
    minutes = math.floor(count / 60)
    seconds = count % 60
    print(f"67- seconds: {seconds}, {type(seconds)}")

    #if len(str(minutes)) == 1 and int(minutes) > 0:
    if minutes == 0:
        minutes = "00"
    elif minutes < 10:
        #minutes = "0" + str(minutes)
        minutes = f"0{minutes}"

    #if len(str(seconds)) == 1 and int(seconds) > 0:
    if seconds == 0:
        seconds = "00"
    elif seconds <  10:
        #seconds = "0" + str(seconds)
        seconds = f"0{seconds}"

    # the canvas.itemconfig allows us to use the timer to count down on the GUI
    #new_count = str(minutes) + ":" + str(seconds)
    print(f"85- minutes: {minutes}")
    print(f"86- seconds: {seconds}, {type(seconds)}")
    #print(f"87- new_count: {new_count}")
    #canvas.itemconfig(timer_text, text=count)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        # print(f"38- count: {count}")
        # count -= 1
        # print(f"40- count: {count}")
        #window.after(1000, count_down, count - 1)
        window.after(10, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
#window.config(padx=50, pady=50, bg=YELLOW)
#window.config(padx=30, pady=30, bg=YELLOW)
window.config(padx=10, pady=50, bg=YELLOW)


def reset_click():
    print("Reset clicked")

# def set_timer_label(label,color):
#     # title_label = Label(text="Timer", font=(FONT_NAME, 60))
#     # title_label.config(fg=GREEN, bg=YELLOW)
#     # title_label.grid(column=1, row=0)
#
#     # clear the label
#     title_label = Label(text="            ", font=(FONT_NAME, 60))
#     title_label.config(fg=color, bg=YELLOW)
#     title_label.grid(column=1, row=0)
#
#     # set the label according to function input
#     title_label = Label(text=label, font=(FONT_NAME, 60))
#     title_label.config(fg=color, bg=YELLOW)
#     title_label.grid(column=1, row=0)
#
# set_timer_label("Timer",GREEN)

title_label = Label(text="Timer", font=(FONT_NAME, 60))
title_label.config(fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

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