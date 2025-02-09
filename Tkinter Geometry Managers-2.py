import tkinter
from tkinter import *
window =  Tk()
window.title("Grid System")
window.geometry("200x300")
window.configure(bg ="red" )
frame1 =  Frame(window,relief="ridge",bg = "skyblue", width= 300, height = 200)
frame1.pack()
def greet():
    name = entry1.get()
    greeting = 'welcome' + name + "log in succesfull"
    text1.delete("1.0","end")
    text1.insert("1.0",greeting)

label1 = Label(frame1, text = "username", bg = "skyblue", fg = "red")
label2 = Label(frame1, text = "password", bg = "skyblue", fg = "red")
entry1 = Entry(frame1)
entry2 = Entry(frame1, show = "*")
button1 = Button(frame1, text = "login ", bg = "pink", command = greet)

label1.place(x =10, y = 10)
label2.place(x = 10, y = 40)
entry1.place(x = 100, y = 10)
entry2.place(x = 100, y = 40)
button1.place(x = 150, y= 80)


text1 = Text(window, relief = "groove", bd = 3, bg = "yellow")
text1.pack(pady = 10)