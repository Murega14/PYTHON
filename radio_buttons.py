from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

window = Tk()
window.geometry("750x484")
style = Style()


pizzaimage = PhotoImage(file='pizza-weird.gif')
hamburgerimage = PhotoImage(file="hamburger.gif")
hotdogimage = PhotoImage(file="hotdog.gif")
foodimages = [pizzaimage, hamburgerimage, hotdogimage]

x =IntVar()

for index in range(len(food)):
    radiobuttton = Radiobutton(window,
                             text=food[index],
                             variable=x,
                             value=index,
                             padx=25,
                             font=("arial",15),
                             image=foodimages[index],
                             compound= LEFT,
                             indicatoron=0,
                             width=375,
                             )
    radiobuttton.pack(anchor=W,padx=15,pady=20)


window.mainloop()