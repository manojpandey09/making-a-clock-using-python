from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("pandey_clock")



def time():
    string = string = strftime('%H:%M:%S %p')
    Label.config(text = string)
    Label.after(1000,time)

Label = Label(root,
              font=("ds-digital", 250),
               background= 'orange' , 
               foreground= 'black')


Label.pack(anchor='center') 
time()
mainloop()  


