"""
program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def main():
    # using list concept
    temp = []
    for i in range(2000, 3201):
        if (i%7) == 0 and (i%5) != 0:
            temp.append(i)
    print(temp)


def main2():
    # without using list concept
    result = ""
    for i in range(2000, 3201):
        if (i%7) == 0 and (i%5) != 0:
            if result == "":
                result = str(i)
            else:
                result = result + "," + str(i)
    print(result)


def main3():
    # using join method
    l = []
    for i in range(2000, 3201):
        if (i % 7 == 0) and (i % 5 != 0):
            l.append(str(i))
    print(','.join(l))


if __name__ == "__main__":
    main()
    main2()
    main3()


