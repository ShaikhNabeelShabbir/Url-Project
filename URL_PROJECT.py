import function as purl
import tkinter
from tkinter import ttk
from tkinter import *


def QR_act():
    X = Link_ent.get()
    purl.get_QR(X)


def Shorten_act():
    Y = Link_ent.get()
    mssg = purl.get_shortener(Y)
    root = tkinter.Tk()
    T = tkinter.Text(root, height=2, width=30)
    T.pack()
    T.insert(tkinter.END, mssg)
    tkinter.mainloop()


window = Tk()
window.title("URL Toolkit")
window.geometry('400x400')
window.configure(background='white')
Link_lbl = Label(window, text="Enter Your URL", fg='Black',
                 font=("calibri", 16)).grid(row=0, column=0)

Link_ent = Entry(window, font=("calibri", 16))
Link_ent.grid(row=2, column=0)

QR_btn = Button(window, text="Generate QR", fg='blue',
                command=QR_act)
QR_btn.grid(row=3, column=0)

Short_btn = Button(window, text="Shorten", fg='blue',
                   command=Shorten_act)
Short_btn.grid(row=4, column=0)

window.mainloop()
