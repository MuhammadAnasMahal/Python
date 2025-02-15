from tkinter import *
window = Tk()
window.title("event handler")
window.geometry("200x200")
window.configure(bg = "lightcyan")

def handle_click(event):
    print("the button is clicked")

def key_pressed(event):
    print(event.char)
window.bind("<Key>", key_pressed)
Button1 = Button(window,text = "click me", bg = "brown", fg = "white")
Button1.place(x = 80, y = 80)
Button1.bind("<Button-1>", handle_click)

window.mainloop()