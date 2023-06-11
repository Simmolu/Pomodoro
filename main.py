from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = '✔'
POM_NUM = 0
text = ''
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global POM_NUM
    mr_screen.after_cancel(timer)
    checks.config(text='')
    timer_label.config(text='Timer')
    canvas.itemconfig(timer_text, text="00:00")
    POM_NUM = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global POM_NUM
    global text
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    POM_NUM += 1
    if POM_NUM % 2 != 0:
        timer_label.config(text='WORK TIME.')
        # time = work_time
        count_down(work_time)
    elif POM_NUM == 8:
        timer_label.config(text='Take a long rest.', fg=RED)
        text += '✔'
        checks.config(text=text)
        count_down(long_break)
        return
    elif POM_NUM % 2 == 0:
        timer_label.config(text='Short break!', fg=PINK)
        # time = short_break
        count_down(short_break)
        text += '✔'

    checks.config(text=text)









# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    count_min = count // 60
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer = mr_screen.after(1000, count_down, count-1)
    else:
        mr_screen.lift()
        mr_screen.attributes('-topmost', True)
        mr_screen.after_idle(mr_screen.attributes, '-topmost', False)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

mr_screen = Tk()


# SCREEN
mr_screen.title('Pomodoro')
mr_screen.config(padx=100, pady=50, bg=YELLOW)



print(POM_NUM)
# TOMATO PICTURE
tomato = PhotoImage(file='tomato.png')  # PhotoImage reads photo file to get right type for canvas

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
canvas.grid(column=1, row=1)

# TIMER
timer_label = Label(text='Timer')
timer_label.config(font=(FONT_NAME, 50, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

# START BUTTON

start_button = Button()
start_button.config(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

# RESET BUTTON
reset_button = Button()
reset_button.config(text='Reset', command=reset)
reset_button.grid(column=2, row=2)

# CHECKMARKS
checks = Label()
checks.grid(column=1, row=3)
checks.config(bg=YELLOW, fg=GREEN)






mr_screen.mainloop()

