from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("messagebox")
window.geometry("300x300")
window.configure(bg = "teal")

def msg():
    messagebox.showwarning("alert", "stop!! Virus Found")

Button1 = Button(window,text = "click me", bg = "brown", fg = "white", command = msg )
Button1.place(x = 80, y = 80)


window.mainloop()