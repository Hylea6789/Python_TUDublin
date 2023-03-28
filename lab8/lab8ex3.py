#######################
# Name : Sean GRIFFIN
# Date : 21/03/23
#######################

# dictionary to store all the logins and passwords
LOGIN = {"student1": "networking101",
         "student2": "networking102",
         "student3": "networking103"}


def enter_username():
    # asks the user to input username. Checks if the username exist

    # asks the user to enter a username
    username = input("Please, enter your username : ")
    username_found = False

    # checks if username is a valid key of dictionnary LOGIN
    if username in LOGIN:
        username_found = True

    # returns the username entered and if the username was found
    return username, username_found


def enter_psswd(username):
    psswd_correct = False
    counter = 5

    # while the password is false and the user hasn't input wrongly 5 times the password
    while counter > 0 and not psswd_correct:
        psswd_entered = input("enter your password : ")

        # if password entered is the value in the dictionary LOGIN for the username entered
        if psswd_entered == LOGIN[username]:  # password valid => breaks the loop
            psswd_correct = True
            break
        else:  # password invalid
            counter -= 1  # the user have one less attempt
            print("Invalid password -", counter, "remaing attempts")

    # returns if password entered was valid
    return psswd_correct


if __name__ == '__main__':
    # asks the user to enter a username
    username, username_correct = enter_username()

    # if username entered exists
    if username_correct:
        print("Welcome ", username)

        # asks the user to enter the password associated with the username
        psswd_correct = enter_psswd(username)
        if psswd_correct:
            print("Your password is correct, you successfully logined")
        else:
            print("ERROR : too  many failed attempts")
    else:
        print("ERROR : username not found")