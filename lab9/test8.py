def pass_mark_40(pass_mark_dic):

    # initialize a list with courses that have a pass mark of 40
    pass_mark_40 = []
    for item in pass_mark_dic.items():
        # if the course has a pass mark of 40
        if item[1] == 40:
            pass_mark_40.append(item[0])
    return pass_mark_40


if __name__ == '__main__':
    # initialize pass mark dictionary
    pass_mark_dic = {
        "Maths": 60,
        "Electronics": 50,
        "Physics": 40,
        "Programming": 40,
        "Networking": 70
    }
    print("pass mark table : ", pass_mark_dic)

    # creates a list with courses that have a pass mark of 40
    pass_mark_40 = pass_mark_40(pass_mark_dic)
    print("these courses have a pass mark of 40 : ", pass_mark_40)