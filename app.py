from tkinter import *             # Sab kuch import karte hain tkinter module se (basic GUI tools jaise Button, Label, etc.)
from tkinter.ttk import *         # ttk se modern themed widgets import karte hain

from time import strftime         # strftime time ko formatted string me convert karta hai

# GUI window banate hain
root = Tk()                       # Main window create hoti hai
root.title("CLOCK")              # Window ka title set karte hain

# Time update karne ka function
def time():
    string = strftime('%H:%M:%S %p')     # Current time ko HH:MM:SS AM/PM format me convert karte hain
    label.config(text=string)            # Label ke text ko update karte hain with current time
    label.after(1000, time)              # Har 1000 milliseconds (1 second) baad time() function fir call hota hai

# Label create karte hain jo clock dikhayega
label = Label(                           # Label widget banate hain
    root,                                # Root window ke andar
    font=("ds-digital", 80),             # Font style aur size set karte hain
    background="black",                  # Background color set karte hain
    foreground="lime"                    # Text color set karte hain
)
label.pack(anchor='center')              # Label ko window ke center me place karte hain

time()                                   # Clock chalu karne ke liye function call karte hain

mainloop()                               # Main GUI loop chalu karte hain — ye window ko zinda rakhta hai
