
# String input. The string is converted to lowercase to only have to detect the character t
string_entered = input("enter a string : ").lower()
count = 0

# checks if each character of the string is a 'T'
for char in string_entered:
    if char == 't':
        count += 1

# displays the numbre of string
print("there is", count, "'T' in the string", string_entered)