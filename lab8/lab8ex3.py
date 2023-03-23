LOGIN = {"student1": "networking101",
         "student2": "networking102",
         "student3": "networking103"}


def enter_username():
    username = input("Please, enter your username : ")
    username_found = False

    if username in LOGIN:
        username_found = True

    return username, username_found


def enter_psswd(username):
    psswd_correct = False
    counter = 5
    while counter > 0 and not psswd_correct:
        psswd_entered = input("enter your password : ")
        if psswd_entered == LOGIN[username]:  # password valid => breaks the loop
            psswd_correct = True
            break
        else:  # password invalid
            counter -= 1  # the user have one less attempt
            print("Invalid password -", counter, "remaing attempts")

    return psswd_correct


if __name__ == '__main__':
    username, username_correct = enter_username()
    if username_correct:
        print("Welcome ", username)
        psswd_correct = enter_psswd(username)
        if psswd_correct:
            print("Your password is correct, you successfully logined")
        else:
            print("ERROR : too  many failed attempts")
    else:
        print("ERROR : username not found")