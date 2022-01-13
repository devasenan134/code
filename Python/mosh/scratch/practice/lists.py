# python 3.7.1
'''
numbers = [23,13,67,56,47,87,93,23,56,43,23]
numbers2 = []
for i in numbers:
    if i not in numbers2:
        numbers2.append(i)
print(numbers2)
'''

numbers = [23, 13, 67, 56, 47, 87, 93, 23, 43, 23]
num = numbers[0]
rep = 0
for i in range(len(numbers)-1):
    if numbers[i] == num:
        rep += 1
        print("ulla", numbers[i], "reps", rep)
    if rep > 1:
        numbers.pop(i)
print(numbers)
