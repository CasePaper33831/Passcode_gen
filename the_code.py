#imports, nothing fun here
import string
import random
import tkinter as tk
from tkinter import messagebox

# all the characters needed for passcode generation
characters = string.digits + string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*()_+-=[]{;:,}.<>/?"

# just defining the inputs for passcode generation
def passcode_length():
    return int(input("Please enter passcode length in numbers with no commas (minimum value 12): "))
def passcode_iteration():
    return int(input("Please input the number of passcode variants with no commas (minimum value 0): "))

# create output popup
root = tk.Tk()
root.withdraw()
length = passcode_length()

# checks inputs, spits error code if stuff is not met
# "stuff" == commas, length, numbers only
if length < 12:
    messagebox.showerror("Invalid Input", "Invalid passcode length input. Please enter a number 12 or higher, with no commas.")
else:
    iterations = passcode_iteration()
    if iterations <= 0:
        messagebox.showerror("Invalid Input", "Invalid iteration amount input. Please enter a number 1 or higher, with no commas.")
    else: # actual passcode generation starts here
        passcodes = []
        for i in range(iterations):
            passcode = ''
            while not any(char in passcode for char in "!@#$%^&*()_{+-=[]};:,.<>/?"):
                passcode = ''.join(random.choice(characters) for _ in range(length))
            passcodes.append(passcode)
        #put output(s) into popup
        passcode_message = "\n".join(f"Passcode {i + 1}: {passcode} \n" for i, passcode in enumerate(passcodes))
        messagebox.showinfo("Passcodes", passcode_message)

root.destroy()
