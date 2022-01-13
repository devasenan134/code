# python 3.7.1


def font1(numbers):
    for i in numbers:
        line = ''
        for j in range(0, i):
            line += "*"
        print(line)


def font2(numbers):
    for i in numbers:
        print("*" * i)
