arr = [5, 5, 5, 5, 5]
add = []
l = len(arr)

for i in range(l):
    add1 = 0
    for j in range(l):
        if i != j:
            add1 += arr[j]   
    add.append(add1)

print(add)
min_num = add[0]
max_num = 0
for n in add:
    if n <= min_num:
        min_num = n
    if n >= max_num:
        max_num = n
        
print(min_num, max_num)
