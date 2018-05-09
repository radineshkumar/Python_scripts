"""
a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line
"""


def main():
    result = 1
    usr_input = int(input("Enter the number to find factorial value:\n"))
    for i in range (usr_input, 0, -1):
        result = result * i
    print (result)


if __name__ == "__main__":
    main()
