from tkinter import *
from random import *

def jump():
    b1.place(relx=random(), rely=random())
    
def hello():
    print("Hello")

master = Tk()

b1 = Button(master, text="Wazzzup!!", command=jump)
b1.place(relx=0.5, rely=0.5, anchor= CENTER)

mainloop()
