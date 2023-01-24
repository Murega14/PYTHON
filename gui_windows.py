from tkinter import *
import runpy
import os

#widgets = GUI elements such as buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets
#label = an area widget that holds text/image in a window

window = Tk() #instantiate the window
window.geometry("420x420")
window.title("muregzzzz")

#icon = PhotoImage(file='pexels-pixabay-35967.jpg')
#window.iconphoto(True, icon)
#window.config(background="wheat")

file = open("rockpaperscissors.py")

def click():
    #runpy.os.path("rockpaperscissors.py")
    print("alright")

photo = PhotoImage(file='/home/nyaweed/PYTHON/hehe_max_reasonably_small.gif')
logo = PhotoImage(file='hehe_max_reasonably_small.gif')

label = Label(window,
            #image="pexels-pixabay-35967.jpg",
             text="Hello There",
             font=('Arial',24,'italic'),
             relief=RAISED,
            image=photo,
            compound='bottom')
#label.place(x=0,y=0)
label.pack()

#button = you click it, it does stuff
button = Button(window,
                text="click me",
                command=click,
                image=logo,
                compound='top'
            )
            
button.pack()

window.mainloop() #place window on screen and listen for events

