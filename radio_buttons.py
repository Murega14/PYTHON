from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get() == 0):
      print("you ordered pizza")
    elif(x.get() == 1):
        print("you ordered a hamburger")  
    elif(x.get() == 2):
        print("you ordered a hotdog")
    else:
        print("huh")


window = Tk()
window.geometry("750x484")
#style = Style()
#style.configure('TButton', font=('calibri', 14, "bold"), borderwidth = '4')


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
                             font=("arial",15),
                             image=foodimages[index],
                             compound= LEFT,
                             indicatoron=0,
                             width=375,
                             command=order
                             )
    radiobuttton.pack(anchor=W,padx=15,pady=20)


window.mainloop()