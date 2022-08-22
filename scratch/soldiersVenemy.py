from math import floor
import sys


ep = 0
count = 0

def attack(s):
    global ep, count
    if s <= 0 or ep < 0:
        return count
    else:
        ep = ep-s
        count += 1
        attack(floor(s/2))
        return count

def minAttacks(n, A, P):
    global ep
    ep = P
    A.sort(reverse=True)
    res = 0
    for i in range(n):
        # print("p: ", P)
        res += attack(A[i])
        if ep < 0:
            break

    # print("\n res: ")
    if ep < 0:
        return res
    else:
        return -1



# n = 4
# A = [1, 2, 4, 8]
# P = 100
# print(minAttacks(n, A, P))