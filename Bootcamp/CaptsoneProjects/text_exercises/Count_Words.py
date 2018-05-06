'''
Counts the number of individual words in a string.
'''


def count_words(str):
    s_split = str.split(" ")
    return len(s_split)


user_input = input("Enter the string: \n")
result = count_words(user_input)
print("The number of individual words in the string: " + str(result))