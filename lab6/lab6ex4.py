#######################
# Name : Sean GRIFFIN
# Date : 28/02/23
#######################

def main():
    # inputs a list of word
    word_list = input_list_of_word()

    print("Word list :", word_list)

    # checks if one or more words starts with "IP"
    start_ip(word_list)

    # sorts the list of words.
    word_list.sort()

    print("Sorted word list :", word_list)

    # prints the three first words of the list
    print("First three word :", word_list[:3])


# Checks if a word starts with IP
def start_ip(word_list):
    # checks each word of the list
    for word in word_list:
        # If the two first characters of the word are "IP"
        if word[:2] == "IP":
            print('"IP" found in word {0}'.format(word))


# Function to that allow the user to input 6 words
def input_list_of_word():
    has_not_six_word = True

    # While less than 6 words are inputed
    while has_not_six_word:
        phrase = input("enter a phrase containing at least 6 words : ")

        # Breaks the phrase in a list of words
        word_list = phrase.split()

        # If there are more than 6 words in the phrase
        if len(word_list) >= 6:
            has_not_six_word = False
        else:
            print("ERROR : he function contains less than 6 words")

    return word_list


if __name__ == '__main__':
    main()
