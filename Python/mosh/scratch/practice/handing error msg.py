# python 3.7.1

try:
    age = int(input('age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('age cannot be zero')
except ValueError:
    print('invalid value')
