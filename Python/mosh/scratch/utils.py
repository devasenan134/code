def maxi(a, b):
    if a > b:
        return f'{a} is the maximum value'
    elif a == b:
        return f'both {a},{b} are same values'
    else:
        return f'{b} is the maximum value'


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def shownumbers(limit):
    for i in range(0, limit):
        if i == 0:
            print(i, " Zero")
        elif i % 2 == 0:
            print(i, " Even")
        else:
            print(i, " Odd")


def multiples(limit):
    add = 0
    for i in range(0, limit+1):  # with respect to the example given in the question
        if i % 3 == 0 or i % 5 == 0:
            add += i
            print(i)
    return add


def show_stars(rows):
    for i in range(1, rows+1):
        print("*" * i)


def prime_numbers(limit):
    try:
        for i in range(2, limit+1):
            for j in range(2, i):
                if i % j == 0:
                    print(i, 'prime illa')
                    break
            else:
                print(i, 'prime')
    except ZeroDivisionError:
        print("none")


def find_max(num):
    maxno = num[0]
    for no in num:
        if no > maxno:
            maxno = no
    return maxno


class WeightConverter:
    def lbs_to_kg(self, weight):
        return weight * 0.45

    def kg_to_lbs(self, weight):
        return weight / 0.45
