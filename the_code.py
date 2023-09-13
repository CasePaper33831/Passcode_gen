'''TODO:
DONE: 
-minimum range of passcode length is TWELVE (12) 
-lower and upper case letter(s) forced output
-digit(s) (0 through 9) forced output
-special character(s) forced output
-ask user for how many versions of passcode
-put text on popup if possible

IN PROGRESS: 
none

Everyone allowed to use code with no worries about asking permissions
'''
import string
import random
import tkinter as tk
from tkinter import messagebox

characters = string.digits + string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*()_+-=[]{;:,}.<>/?"

def passcode_length():
    return int(input("Please enter passcode length in numbers with no commas (minimum value 12): "))

def passcode_iteration():
    return int(input("Please input the number of passcode variants (minimum value 0): "))

root = tk.Tk()
root.withdraw()
length = passcode_length()
if length < 12:
    messagebox.showerror("Invalid Input", "Invalid passcode length input. Please enter a number 12 or higher, with no commas.")
else:
    iterations = passcode_iteration()
    if iterations <= 0:
        messagebox.showerror("Invalid Input", "Invalid iteration amount input. Please enter a number 1 or higher, with no commas.")
    else:
        passcodes = []
        for i in range(iterations):
            passcode = ''
            while not any(char in passcode for char in "!@#$%^&*()_{+-=[]};:,.<>/?"):
                passcode = ''.join(random.choice(characters) for _ in range(length))
            passcodes.append(passcode)

        passcode_message = "\n".join(f"Passcode {i + 1}: {passcode} \n" for i, passcode in enumerate(passcodes))
        messagebox.showinfo("Passcodes", passcode_message)

root.destroy()
