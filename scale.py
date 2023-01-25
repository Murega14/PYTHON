from tkinter import *

def submit():
    print("the temperature is: ", str(scale.get()), "degrees")

window = Tk()

hotimage = PhotoImage(file='flame.gif')
hotlabel = Label(image=hotimage,compound=LEFT)
hotlabel.pack()

scale = Scale(window,
            from_=100,
            to=0,
            length=300,
            orient=HORIZONTAL,
            font=('Arial', 14),
            tickinterval = 10,
            showvalue=0,
            resolution = 5,
            troughcolor = "blue",
            fg = "red",
            bg = "black")
scale.pack()

coldimage = PhotoImage(file='snowflake.gif')
coldlabel = Label(image=coldimage, compound=RIGHT)
coldlabel.pack()

button = Button(window, text='submit',command=submit, compound=BOTTOM)
button.pack()

window.mainloop()
