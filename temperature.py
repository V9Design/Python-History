from tkinter import *
import tkinter.font

root = Tk()
root.title("tempconverter")
root.geometry("400x400")

# set font size
thefont = tkinter.font.Font(size=15)

#create a new frame
nwframe = LabelFrame(root,text="temp converter", padx=10,pady=10)
nwframe.place(x =15 , y =10 )

#title and text
title = Label(nwframe,text="Temperature").grid(row = 0, columnspan=3)
equals = Label(nwframe, text="=").grid(row = 1, column=1)

#create a number input box
e1 = Entry(nwframe,width=15)
e2 = Entry(nwframe,width=15)
e1["font"] = thefont
e2["font"] = thefont
e2.insert(0, "0")
e1.grid(row=1,column=0)
e2.grid(row=1, column=2)

# write down formulas and all functions
rmslbl = Label(nwframe,text="Formula",bg="yellow")
rmslbl.place(x = 1, y =90)

rmsnya = Label(nwframe,text="(...°C x 9/5) + 32 = ...°F")
rmsnya.place(x = 50, y=90)

chek = {"formula","yes"}

def formula(rm):
    # delete the writing in box 2
    e2.delete(0,END)

    # get the value from the box
    box1 = cliked.get()
    box2 = cliked2.get()
    number1 = int(e1.get())

    # delete previous post
    global rmsnya
    if "formula" in chek:
        rmsnya.place_forget()
    else:
        pass

    # write formulas and determine calculations
    if box1 =="celsius" and box2 == "fahrentheit":
        rmsnya =Label(nwframe,text="("+e1.get()+"°C x 9/5) + 32 = ... °F")
        count = (number1 * 9/5) + 32
    elif box1 =="celsius" and box2 == "kelvin":
        rmsnya =Label(nwframe,text=e1.get()+"°C + 273.15 = ... K")
        count = (number1 + 273.15)
    elif box1 =="celsius" and box2 == "reamur":
        rmsnya =Label(nwframe,text="(4/5 x "+e1.get()+"°C) = ... R")
        count = (4/5 * number1)
    elif box1 =="fahrentheit" and box2 == "celsius":
        rmsnya =Label(nwframe,text="("+e1.get()+"°F - 32) x 5/9 = ... °C")
        count = (number1 - 32) * 5/9
    elif box1 =="fahrentheit" and box2 == "kelvin":
        rmsnya =Label(nwframe,text="("+e1.get()+"°F - 32) x 5/9 + 273.15 = ... K")
        count = (number1 - 32) * 5/9 + 273.15
    elif box1 =="fahrentheit" and box2 == "reamur":
        rmsnya =Label(nwframe,text="("+e1.get()+"F - 32) x 4/9 = ... R")
        count = (number1 - 32) * 4/9
    elif box1 =="reamur" and box2 == "celsius":
        rmsnya =Label(nwframe,text="5/4 x "+e1.get()+"R) = ... °C")
        count = (5/4 * number1)
    elif box1 =="reamur" and box2 == "fahrentheit":
        rmsnya =Label(nwframe,text="(9/4 x "+e1.get()+"R) + 32 = ... F")
        count = (9/4 * number1) + 32
    elif box1 =="reamur" and box2 == "kelvin":
        rmsnya =Label(nwframe,text="(5/4 x"+e1.get()+"R) + 273 = ... K")
        count = (5/4 * number1) + 273
    elif box1 =="kelvin" and box2 == "celsius":
        rmsnya =Label(nwframe,text=e1.get()+"K - 273.15 = ... °C")
        count = (number1 - 273.15)
    elif box1 =="kelvin" and box2 == "fahrentheit":
        rmsnya =Label(nwframe,text="("+e1.get()+"K - 273.15) x 9/5 + 32 = ... °F ")
        count = (number1 - 273.15) * 9/5 + 32
    elif box1 =="kelvin" and box2 == "reamur":
        rmsnya =Label(nwframe,text="("+e1.get()+"k - 273) x 4/5 = ... R")
        count = (number1 - 273.15) * 4/5
    elif box1 =="celsius" and box2 == "celsius" or box1 == "fahrentheit" and box2 == "fahrentheit" or box1 == "kelvin" and box2 == "kelvin" or box1 == "reamur" and box2 == "reamur":
        rmsnya =Label(nwframe,text="There is no Formula")
        count = number1
    result = count
    e2.insert(0, result)
    rmsnya.place(x = 50, y=90)



option = ["celsius","fahrentheit","kelvin","reamur"]
cliked = StringVar()
cliked.set(option[0])
drop = OptionMenu(nwframe,cliked,*option,command=formula)
drop.config(width=20)
drop.grid(row =2,column=0)


cliked2 = StringVar()
cliked2.set(option[1])
drop2 = OptionMenu(nwframe,cliked2,*option,command=formula)
drop2.config(width=20)
drop2.grid(row =2,column=2)

#make the button calculate
btn = Button(nwframe,text="count",command=lambda:formula("calculate"))
btn.grid(row = 3,column=2)

root.mainloop()