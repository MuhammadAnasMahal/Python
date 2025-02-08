from tkinter import*

win =  Tk()
win.geometry("400x300")
win.title("greetings")

def mygreet():
    name = Entry1.get()
    greetings = 'Welcome' + name
    text1.delete("1.0","end")
    text1.insert('1.0',greetings)
    
Label1 = Label(text = "Name", fg = "lightblue")
Label1.pack()
Entry1 = Entry()
Entry1.pack()
Button1 = Button(text = "Click Me", fg = "lightblue", command = mygreet)
Button1.pack()
text1 = Text(width = 100, height = 3, border = 2)
text1.pack() 

win.mainloop()