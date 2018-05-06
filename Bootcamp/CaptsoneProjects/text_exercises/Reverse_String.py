# Enter a string and the program will reverse it and print it out.

string_value = 'Python exercise'


# function1
def implementation1():
    return string_value[::-1]


def implementation2():
    result =""
    for char in range(len(string_value),0,-1):
        result += string_value[char-1]
    return result


def implementation3():
    reverse_string = ''
    num = len(string_value)-1
    for char in string_value:
        reverse_string += string_value[num]
        num -= 1
    return reverse_string

print(implementation1())
print(implementation2())
print(implementation3())