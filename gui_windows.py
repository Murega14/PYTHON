from tkinter import *
import runpy
import os

#widgets = GUI elements such as buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets
#label = an area widget that holds text/image in a window
#entry widget = textbox that accepts a single line of user input

window = Tk() #instantiate the window
#window.geometry("420x420")
window.title("muregzzzz")

#icon = PhotoImage(file='pexels-pixabay-35967.jpg')
#window.iconphoto(True, icon)
#window.config(background="wheat")

file = open("rockpaperscissors.py")
count = 0

def click():
    global count
    count += 1
    print(count)

def submit():
     username = entry.get()
     print("hello", username)
     #entry.config(state=DISABLED)


def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get()) -1, END)

photo = PhotoImage(file='/home/muregz/PYTHON/hehe_max_reasonably_small.gif')
logo = PhotoImage(file='hehe_max_reasonably_small.gif')

label = Label(window,
            #image="pexels-pixabay-35967.jpg",
             text="Hello There",
             font=('Arial',24,'italic'),
             relief=RAISED,
            image=photo,
            compound='bottom')
#label.place(x=0,y=0)
#label.pack()

entry = Entry(window,
            font=("Arial", 20),
            fg="wheat",
            bg="black",
            #show="*"
            )

entry.pack(side=LEFT)

submit1 = Button(window,text="submit", command=submit)
submit1.pack(side=RIGHT)


delete1 = Button(window,text="delete", command=delete)
delete1.pack(side=RIGHT)

delete1 = Button(window,text="backspace", command=backspace)
delete1.pack(side=RIGHT)

#button = you click it, it does stuff
button = Button(window,
                text="click me",
                command=click,
                image=logo,
                compound='top'
            )
            
#button.pack()



window.mainloop() #place window on screen and listen for events

