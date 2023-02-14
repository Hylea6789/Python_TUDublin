# Initialization of constants
# initialization of the password for the 3 student logins
PSSWD_STUDENT1 = "networking101"
PSSWD_STUDENT2 = "networking102"
PSSWD_STUDENT3 = "networking103"

# initialization of maximum number of password attempts
PSSWD_MAX_ATTEMPTS = 5

# initialization of loop break condition
username_not_found = True


# While the username doesn't match with one of the 3 student logins
while username_not_found:
    # input of username
    username = input("Please, enter your username : ")
    username_not_found = False

    # Checks if username entered is one of three logins
    # If it' the case, inialize the password
    if username == "student1":
        psswd = PSSWD_STUDENT1
    elif username == "student2":
        psswd = PSSWD_STUDENT2
    elif username == "student3":
        psswd = PSSWD_STUDENT3
    else:
        username_not_found = True
        print("Error : Username not found")

# If the loop is breaked, the username is found
print("Welcome -", username, "- please enter your password")


# initialization of counter to the maximum password attempts
counter = PSSWD_MAX_ATTEMPTS

# Password input loop. The loop is break if the password is entered correctly or PSSWD_MAX_ATTEMPTS
while counter > 0:
    psswd_entered = input("enter your password : ")
    if psswd_entered == psswd:  # password valid => breaks the loop
        break
    else:   # password invalid
        counter -= 1    # the user have one less attempt
        print("Invalid password -", counter,"remaing attempts")


if counter > 0:     # more than one attempts remaining when exiting the loop => password valid
    print("Password valid, successfully logged in")
else:   # No attempts remaining when exiting the loop => password invalid
    print("Authentication failed, too many attempts")