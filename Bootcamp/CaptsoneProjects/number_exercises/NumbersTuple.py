"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and
a tuple which contains every number.
"""

def main():

    usr_input = input("Enter the numbers in comma format:\n")

    test = usr_input.split(",")
    print(test)
    print(tuple(test))


if __name__ == "__main__":
            main()