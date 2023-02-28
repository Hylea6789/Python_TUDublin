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

    # sorts the list of words
    word_list.sort()


    print("Sorted word list :", word_list)
    print("First three word :", word_list[:3])


def start_ip(word_list):
    for word in word_list:
        if word[:2] == "IP":
            print('"IP" found in word {0}'.format(word))


def input_list_of_word():
    has_not_six_word = True
    while has_not_six_word:
        phrase = input("enter a phrase containing at least 6 words : ")
        word_list = phrase.split()
        if len(word_list) >= 6:
            has_not_six_word = False
        else:
            print("ERROR : he function contains less than 6 words")

    return word_list


if __name__ == '__main__':
    main()
