from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=" :
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else :
            try :
               value = eval(screen.get())
            except Exception as e :
                print(e)
                value = "Error"
             
        scvalue.set(value)
        screen.update()
    elif text == "c" :
        scvalue.set("")
        screen.update()
    else :
        scvalue.set(scvalue.get() + text)
        screen.update()
        
root = Tk()
root.geometry("350x510")
root.title("calculator")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root , textvar = scvalue , font="lucida 40 bold")
screen.pack(fill=X , ipadx=8 , padx=10 ,pady=10)
f = Frame(root , bg="gray")
b = Button(f , text="9" , padx=28 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT ,padx=10 , pady=5)
b.bind("<Button-1>" , click)
b = Button(f , text="8" , padx=28 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT , padx=10 ,pady=5)
b.bind("<Button-1>" , click)
b = Button(f , text="7" , padx=28 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT , padx=10 , pady=5)
b.bind("<Button-1>" , click)

f.pack()

f = Frame(root , bg="gray")
b = Button(f , text="6" , padx=28 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT ,padx=10 , pady=5)
b.bind("<Button-1>" , click)
b = Button(f , text="5" , padx=28 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT , padx=10 ,pady=5)
b.bind("<Button-1>" , click)
b = Button(f , text="4" , padx=28 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT , padx=10 , pady=5)
b.bind("<Button-1>" , click)

f.pack()

f = Frame(root , bg="gray")
b = Button(f , text="3" , padx=28 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT ,padx=10 , pady=5)
b.bind("<Button-1>" , click)
b = Button(f , text="2" , padx=28 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT , padx=10 ,pady=5)
b.bind("<Button-1>" , click)
b = Button(f , text="1" , padx=28 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT , padx=10 , pady=5)
b.bind("<Button-1>" , click)

f.pack()
f = Frame(root , bg="gray")
b = Button(f , text="0" , padx=29 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT ,padx=11 , pady=5)
b.bind("<Button-1>" , click)
b = Button(f , text="-" , padx=29 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT , padx=11 ,pady=5)
b.bind("<Button-1>" , click)
b = Button(f , text="*" , padx=29 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT , padx=10 , pady=5)
b.bind("<Button-1>" , click)

f.pack()
f = Frame(root , bg="gray")
b = Button(f , text="/" , padx=28 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT ,padx=11 , pady=5)
b.bind("<Button-1>" , click)
b = Button(f , text="c" , padx=28 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT , padx=11 ,pady=5)
b.bind("<Button-1>" , click)
b = Button(f , text="=" , padx=28 , pady=10 , font="lucida 20 bold")
b.pack(side=LEFT , padx=11 , pady=5)
b.bind("<Button-1>" , click)

f.pack()
root.mainloop()
