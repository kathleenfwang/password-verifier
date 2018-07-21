###############################################################################
# CS 21a Python Programming: Lab 2
# Description:  Programming with Loops and Functions
# Name: Kathleen Wang
# Date : July 17, 2018
###############################################################################

"""The Program Spec

Write a program using loops and functions that asks for a password, and then asks the user to confirm the password chosen.  Your solution will verify that both user passwords entered match.  Your program must also validate that the new password follows these rules:

The password must be at least 8 characters long
The password must have at least one uppercase and one lowercase letter
The password must have at least one digit
Re-prompt the user if either 1) the two passwords entered do not match or if  2) the password does not satisfy all the rules stated 
Here are some other requirements:

Create constants versus using literals in your source code (i.e. for minimum password length)
Include a function that checks whether a password is valid
Include a loop that will continue to prompt the user until a valid password is entered
"""

MIN = 8 
valid = False 

def check_valid(user_pass):
    count = 0; 
    if (len(user_pass) < MIN):
        print('Password needs to be at least 8 letters.')
        print('Password also needs a number and capital letter.')
        return False 

    for x in user_pass:
        if (ord(x) >= 65 and ord(x) <= 90):
            count = count + 1 
        try:
            int(x)
            if count < len(user_pass) + 1:
                count = count + len(user_pass) +1 
        except:
            continue
     
    if count >= len(user_pass) + 2:
        return True 
    if count > len(user_pass):
        print('Password needs an upper case letter.')
        return False 
    elif count == 0:
        print('Password needs a number and an upper case letter.')
    else:
        print('Password needs a number.')
        return False
		 
while not valid: 
    user_pass = input('Enter a new password:')

    if check_valid(user_pass):
        while not valid:
            second_pass = input('Please re-enter your password:')

            if second_pass == user_pass:
                print('You have submitted your password.')
                valid = True
            else:
                print('Your passwords do not match. Please try again.')
            
    else:
        print('Please try again.')
"""Run
Enter a new password: Kathleen1
Please re-enter your password: Kathleen1
You have submitted your password.

Enter a new password: hello
Password needs to be at least 8 letters.
Password also needs a number and capital letter.
Please try again.

Enter a new password: hellothere
Password needs a number and an upper case letter.
Please try again.

Enter a new password: hellothere1
Password needs an upper case letter.
Please try again.

Enter a new password: Hellothere1
Please re-enter your password: hellothere1
Your passwords do not match. Please try again.
Please re-enter your password: Hellothere1
You have submitted your password.

Run"""
 
 