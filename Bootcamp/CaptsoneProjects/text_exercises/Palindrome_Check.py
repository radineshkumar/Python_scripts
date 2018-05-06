'''
Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like “racecar”
'''


def implementation1(str):
    return str == str[::-1]


def implementation2(str):
    reverse_str = ''
    num = len(str)-1
    for c in str:
        reverse_str += str[num]
        num -= 1
    return str == reverse_str


user_input = input('Enter the string: \n')

result1 = implementation1(user_input)
if result1 is True:
    print("Result - Implementation1: Text is a palindrome")
else:
    print("Result - Implementation1: Text is not a palindrome")
print("###############################")
result2 = implementation2(user_input)
if result2 is True:
    print("Result - Implementation2: Text is a palindrome")
else:
    print("Result - Implementation2: Text is not a palindrome")