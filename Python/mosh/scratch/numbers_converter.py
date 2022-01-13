# python 3.7.1


def numbers_converter(phno):
    numbers = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',  '8': 'eight',  '9': 'nine',  '0': 'zero'}
    line = ''
    for number in phno:
        line += numbers[number] + " "
    return line
