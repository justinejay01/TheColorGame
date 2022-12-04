from tkinter import *
import random
from tkinter import messagebox

colorg = Tk()   
colorg.title("The Color Game")
w = 750
h = 500
 
screen_width = colorg.winfo_screenwidth()
screen_height = colorg.winfo_screenheight()

x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
 
colorg.geometry('%dx%d+%d+%d' % (w, h, x, y))

timr = 30

def start(e):
    txt0.config(text="")
    if(timr==30):
        countdown()
    
    nxtcolor()

def nxtcolor():
    global s
    global timr

    if timr>0:
        i.focus_set()
        if(i.get().lower()==colors[1].lower()):
            s+=1
        
        i.delete(0, END)
        random.shuffle(colors)
        txt1.config(fg=str(colors[1]), text=str(colors[0]))
        scoret = Label(text="Score: ", font=("Aria", 15))
        scoret.place(x=260, y=80)
        scores = Label(text=str(s), font=("Aria", 15))
        scores.place(x=330, y=80)
    else: 
        messagebox.showinfo('Game Over', 'Your time is up and your total score is ' + str(s))

def countdown():
    global timr

    timrt = Label(colorg, text="Time: ", font=('Aria', 15))
    timrt.place(x=260, y=110)
    timrs = Label(colorg, text=str(timr), font=('Aria', 15))

    if (timr>=0):
        timr-=1
        timrs.place(x=330, y=110)
        timrs.after(1000, countdown)
        

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'pink', 'white', 'black', 'brown']
s = 0

txt = Label(colorg, text="Type the name of the color, and not the word text", font=('Aria', 20))
txt.place(x=70, y=30)
txt0 = Label(colorg, text="Press Enter to Start", font=('Aria', 15))
txt0.place(x=260, y=80)

i = Entry(colorg, font=('Aria', 15))
i.place(x=260, y=400)

txt1 = Label(colorg, font=('Aria', 100))
txt1.place(x=160, y=150)

colorg.bind('<Return>', start)
i.focus_set()
colorg.mainloop()