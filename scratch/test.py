
res = []

s = input()
k = input()

for i in range(len(s) - len(k)+1):
    j = 0
    start = 0
    end = -1
    while(j <= len(k)-1 and s[i+j]==k[j]):
        if j == 0:
            start = i
        j+=1
    if j == len(k):
        print(i)
        end = i+j-1
        res.append([start, end])
if len(res) == 0:
    res = [(-1, -1)]
print(*res)