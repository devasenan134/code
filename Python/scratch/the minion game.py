str1 = "ANANAS"
l = len(str1)
kevin = []
stuart = []
for _ in range(l) :
    if str1[_] in ["A", "E", "I", "O", "U"] :
        if str1[_] not in kevin :
            kevin.append(str1[_])
    else :
        if str1[_] not in stuart :
            stuart.append(str1[_])
# print(kevin, stuart)

k_index = []
s_index = []

for vowels in kevin :
    k_index.append(str1.find(vowels))
for consonants in stuart :
    s_index.append(str1.find(consonants))

# print(k_index, s_index)

str_kevin = []
str_stuart = []
for index in k_index :
    for i in range(index, l) :
        str_kevin.append(str1[index:i+1])

for index in s_index :
    for j in range(index, l) :
        str_stuart.append(str1[index:j+1])

# print(str_kevin ,str_stuart)

dict_kevin = {}
dict_stuart = {}

for string in str_kevin :
    dict_kevin[string] = 1
for string in str_stuart :
    dict_stuart[string] = 1


# print(dict_kevin, dict_stuart)

for s in dict_kevin :
    dict_kevin[s] = str1.count(s)
for s in dict_stuart :
    dict_stuart[s] = str1.count(s)

print(dict_kevin, dict_stuart)
sum_kevin = sum(dict_kevin.values())
sum_stuart = sum(dict_stuart.values())

if sum_kevin > sum_stuart :
    print("Kevin", sum_kevin)
else :
    print("Stuart", sum_stuart)
# Kevin 12
