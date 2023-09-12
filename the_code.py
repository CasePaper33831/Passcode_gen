'''TODO:
DONE: 
-minnimum range of passcode length is TWELVE (12) 
-lower and upper case letter(s) forced output
-digit(s) (0 through 9) forced output
-special character(s) forced output

IN PROGRESS: 
-ask user for how many versions of passcode
-put text on popup if possible

Everyone allowed to use code with no worries about asking permissions
'''
import string
import random

characters = string.digits + string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*()_+-=[]{;:,}.<>/?"

def passcode_length():
    return int(input("Please enter passcode length in numbers with no commas (minimum value 12): "))

while True:
    length = passcode_length()
    if length < 12:
        print("Invalid input. Please enter a number 12 or higher, with no commas.")
        
    else:
        passcode = ''
        while not any(char in passcode for char in "!@#$%^&*()_{+-=[]};:,.<>/?"):
            passcode = ''.join(random.choice(characters) for i in range(length))
        print(str("Your new passcode is: " + passcode))
        break
