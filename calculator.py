import tkinter as tk

#button click handler
def click(event):
    global expression
    text=event.widget.cget("text")
    if text=="=":
        try:
            result=eval(expression)
            screen_var.set(result)
            expression=str(result)
        except Exception:
            screen_var.set("Error")
            expression=""
    elif text=="C":
        expression=""
        screen_var.set("")
    else:
        expression+=text
        screen_var.set(expression)

#main window
root=tk.Tk()
root.title("Calculator")

expression=""
screen_var=tk.StringVar()

#display
screen=tk.Entry(root,textvar=screen_var,font="Arial 20 bold",justify="right",bd=8,relief="ridge")
screen.pack(fill="both",ipadx=8,pady=10,padx=10)

#buttons
button_frame=tk.Frame(root)
button_frame.pack()

button=[
    ["7","8","9","+"],
    ["4","5","6","-"],
    ["1","2","3","*"],
    ["C","0","=","/"],
]

#color
button_colors={
    "C":{"bg":"red","fg":"white"},
    "=":{"bg":"green","fg":"white"},
    "+":{"bg":"lightblue","fg":"black"},
    "-":{"bg":"lightblue","fg":"black"},
    "*":{"bg":"lightblue","fg":"black"},
    "/":{"bg":"lightblue","fg":"black"},

}

for row in button:
    frame=tk.Frame(button_frame)
    frame.pack(side="top",pady=5)
    for btn_text in row:
        colors=button_colors.get(btn_text,{"bg":"lightgray","fg":"black"})
        b=tk.Button(frame,text=btn_text,font="Arial 18",width=4,height=1,bg=colors["bg"],fg=colors["fg"],bd=3,relief="raised")
        b.pack(side="left",padx=5)
        b.bind("<Button-1>",click)

root.mainloop()