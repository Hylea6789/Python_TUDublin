
# user inputs the code
code = input("enter program code and year : ").lower()

# equals to true if program and year are found
is_find = False

# checks if the user starts by TU716
if code[:5] == "tu716":
    # checks if it include the "year 1", "year 2" or "year 3"
    for i in range(3):
        string_to_find = "year " + str(i)
        # if year isn't found, find function will return -1
        if code.find(string_to_find) != -1:
            is_find = True
            year = i

# if year and program code are found displays a welcome message
if is_find:
    print("Welcome to TU716 in year", year)
else:
    print("ERROR : program or year not found")