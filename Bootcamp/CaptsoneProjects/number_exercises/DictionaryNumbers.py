"""
With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
such that is an integral
number between 1 and n (both included). and then the program should print the dictionary.
"""

def main(val):

    dic_num = dict()

    for i in range(1, val+1):
        dic_num[i] = i*i

    print(dic_num)


if __name__ =="__main__":
    main(int(input("Enter the number:\n")))