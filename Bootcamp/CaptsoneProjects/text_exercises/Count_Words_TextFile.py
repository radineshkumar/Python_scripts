
'''
Counts the number of individual words in a string.
For added complexity read these strings in from a text file and generate a summary
'''

myfile = open("countwords.txt","w+")
myfile.write("Hello this is Dinesh")
myfile.writelines("\nI love Python language")
myfile.writelines("\nIt's fun to learn Python")
myfile.writelines("\nI want to be expert in Python")
myfile.close()

file_content = open("countwords.txt", "r+").read()
file_strings = file_content.replace("\n", " ")
print(file_strings)
file_words = file_strings.split(" ")
print("Number of words present in the strings: " + str(len(file_words)))
dict_words = {}
dup_words = set()
for word in file_words:
    if dict_words.get(word) is not None:
        dict_words[word] = dict_words.get(word)+1
        dup_words.add(word)
    else:
        dict_words[word] = 1
print(dict_words)

# words which appeared more than once
for l in dup_words:
    print("#####################################")
    print("words appeared more than once in the text file: " + l)
    print("words appeared number of times in the text file: " + str(dict_words.get(l)))



# rem_dup = set()
# # remove duplicate words
# for words in file_words:
#     rem_dup.add(words)
#
# print(rem_dup)
