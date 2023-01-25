from tkinter import *

def submit():
    print("the temperature is: ", str(scale.get()), "degrees")

window = Tk()

hotimage = PhotoImage(file='flame.gif')
hotlabel = Label(image=hotimage)
hotlabel.pack()

scale = Scale(window,
            from_=100,
            to=0,
            length=300,
            orient=VERTICAL,
            font=('Arial', 14),
            tickinterval = 10,
            showvalue=0,
            resolution = 5,
            troughcolor = "blue",
            fg = "red",
            bg = "black")
scale.pack()

coldimage = PhotoImage(file='snowflake.gif')
coldlabel = Label(image=coldimage)
coldlabel.pack()

button = Button(window, text='submit',command=submit)
button.pack()

window.mainloop()
