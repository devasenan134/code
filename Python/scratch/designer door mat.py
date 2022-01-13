n, m = input().split()
n = int(n)
m = int(m)
c = ".|."
for i in range(n//2) :
    print((c * i).rjust((m//2)-1,"-")+c+(c * i).ljust((m//2)-1,"-"))
print("WELCOME".center(m, "-"))

for i in range(n//2-1, -1, -1) :
    print((c * i).rjust((m//2)-1,"-")+c+(c * i).ljust((m//2)-1,"-"))
