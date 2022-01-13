def hexa(n):
    num = {10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"}

    if n in num:
        print(num[n], end="")
    else:
        if n >= 16:
            hexa( n // 16)
        print(n % 16, end="")


hexa(17)
