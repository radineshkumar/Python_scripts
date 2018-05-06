'''
Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
'''


class CountVowels():

    def test(self):
        usr_input = input('Enter the string: \n')
        count = 0
        vowel_dic = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

        for char in usr_input.lower():
            if char in {'a', 'e', 'i', 'o', 'u'}:
                count += 1
                vowel_dic[char] += 1

        # print total of each vowels (present or not present in the text)

        print('#####################################')
        print("total 'a' found: {}".format(vowel_dic['a']))
        print("total 'e' found: {}".format(vowel_dic['e']))
        print("total 'i' found: {}".format(vowel_dic['i']))
        print("total 'o' found: {}".format(vowel_dic['o']))
        print("total 'u' found: {}".format(vowel_dic['u']))
        print('#####################################')

        # print total of each vowels (only if present in the text)

        for key, val in vowel_dic.items():
            if vowel_dic.get(key) >= 1:
                print("total '{0}' found: '{1}'".format(key, val))
        print('#####################################')
        return count


c = CountVowels()
print('total vowels present: ' + str(c.test()))