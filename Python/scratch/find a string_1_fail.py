s = "ABCDCDC"
sub = "CDC"
l = len(s)
l1 = len(sub)
a = 0
count = 0
for i in range(l) :
    if sub[0] == s[i] :
        for j in range(l1) :
            #print("j",j , i)
            try :
                if s[i+j] == sub[j] :
                    a = 1
                    #print(s[i+j], i, j, count)
                else :
                    a = 0
            except :
                a = 0
        if a == 1:
            count += 1
    else :
        continue

print(count)
