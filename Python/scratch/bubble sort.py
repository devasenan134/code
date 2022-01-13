a = [3, 6, 2, 1, 9]
n = 5
n_swaps = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            n_swaps += 1
        
print(f"Array is sorted in {n_swaps} swaps")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[n-1]}")
print(a)
