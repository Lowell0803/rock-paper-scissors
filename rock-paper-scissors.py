from tkinter import *
import random

root = Tk()
root.title('Rock Paper Scissors')
root.resizable(0, 0)

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

w = 600
h = 600

x = (sw/2) - (w/2)
y = (sh/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

cv = Canvas(width=w, height=h, borderwidth=0, highlightthickness=0, bg="white")
cv.pack(side='top', fill='both', expand='yes')

player = Label(cv, borderwidth=0, bg="white")
player.place(x=20, y=50)

computer = Label(cv, borderwidth=0, bg="white")
computer.place(x=320, y=50)

rock_img = PhotoImage(file="img/rock.gif")
paper_img = PhotoImage(file="img/paper.gif")
scissor_img = PhotoImage(file="img/scissors.gif")

computer_rock_img = PhotoImage(file="img/rock_computer.gif")
computer_paper_img = PhotoImage(file="img/paper_computer.gif")
computer_scissor_img = PhotoImage(file="img/scissors_computer.gif")

def rock(event):
	global player_choice
	player_choice = 1
	player.configure(image=rock_img)
	match_process()

def paper(event):
	global player_choice
	player_choice = 2
	player.configure(image=paper_img)
	match_process()
    
def scissor(event):
	global player_choice
	player_choice = 3
	player.configure(image=scissor_img)
	match_process()

def match_process():
    com_choice = random.randint(1,3)
    if com_choice == 1:
        computer.configure(image=computer_rock_img)
        computer_rock()
    elif com_choice == 2:
        computer.configure(image=computer_paper_img)
        computer_paper()
    elif com_choice == 3:
        computer.configure(image=computer_scissor_img)
        computer_scissor()

def computer_rock():
    if player_choice == 1:
        lbl_status.config(text="Game Draw")
    elif player_choice == 2:
        lbl_status.config(text="User Wins")
    elif player_choice == 3:
        lbl_status.config(text="Comp Wins")
           
def computer_paper():
    if player_choice == 1:
        lbl_status.config(text="Comp Wins")
    elif player_choice == 2:
        lbl_status.config(text="Game Draw")
    elif player_choice == 3:
        lbl_status.config(text="User Wins")
    
def computer_scissor():
    if player_choice == 1:
        lbl_status.config(text="User Wins")
    elif player_choice == 2:
        lbl_status.config(text="Comp Wins")
    elif player_choice == 3:
        lbl_status.config(text="Game Draw")

lbl_status = Label(cv, text="PLAY NOW!", bg="white", fg="#3f3f3f", font=('Bebas Kai', 40))
lbl_status.place(x=200, y=318)

brown_frame = Frame(cv, bg="#3f3f3f", borderwidth=0, width=600, height=210)
brown_frame.place(x=0, y=395)

choice1_img = PhotoImage(file="img/choice1.gif")
choice1 = Label(cv, image=choice1_img, borderwidth=0)
choice1.place(x=5, y=420)

choice2_img = PhotoImage(file="img/choice2.gif")
choice2 = Label(cv, image=choice2_img, borderwidth=0)
choice2.place(x=205, y=420)

choice3_img = PhotoImage(file="img/choice3.gif")
choice3 = Label(cv, image=choice3_img, borderwidth=0)
choice3.place(x=405, y=420)

choice1.bind('<Button-1>', rock)
choice2.bind('<Button-1>', paper)
choice3.bind('<Button-1>', scissor)

root.iconbitmap("img/rps_icon.ico")
root.mainloop()
