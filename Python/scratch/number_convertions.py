def deci(n):
    
    for i in range(1, n+1):
        o, h, b = "", "", ""
        print(str(i).rjust(l), end=" ")
        o += octal(i)
        print(o, end="")
        print()

def octal(n):
    if n >= 8:
        octal(n // 8)
    return str(n % 8)

def hexa(n, h):
    num = {10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"}

    if n in num:
        h += num[n]
    else:
        if n >= 16:
            hexa( n // 16, h)
        h += str(n % 16)
        if n // 16 ==  0:
            print(h.rjust(l), end=" ")

def bina(n, b):
    if n > 1:
        bina(n // 2, b)
    b += str(n % 2)
    if n // 2 == 0:
        print(b.rjust(l), end="")


n = 17  
l = len(bin(n)[2:])
deci(n)
