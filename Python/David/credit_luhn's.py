def credit_luhns() :
    while True :
        number = input("Number: ")
        l = len(number)
        if l not in [13, 14, 16] :
            print("Invalid")
            continue
        else :
            break

    prop = ""
    if number[0] in ["4"] and l in [13, 16] :
        prop = "VISA"
    #elif number[:2] in ["34", "37"] and l == 15 :
    #   prop = "AMEX"
    elif number[:2] in ["51", "52", "53", "54", "55", "22"] and l == 16 :
        prop = "MASTERCARD"
    elif number[0] in ["3"] and l == 14:
        prop = "DINERS_CLUB"
    else :
        prop = "INVALID"

    # print(number, prop)
    sum1 = ""
    sum2 = []
    for i in range(l) :
        if i > 0  and i % 2 != 0 :
            continue
        else :
            sum1 += str(int(number[i]) * 2)

    for _ in sum1 :
        sum2.append(int(_))
    add = sum(sum2)

    for j in range(l) :
        if j > 0 and j % 2 != 0 :
            add += int(number[j])

    if add % 10 == 0 :
        print(prop)
    else :
        print("INVALID")
    #print(sum1, sum2, add)

    
opt = "y"
while opt == "y" :
    credit()
    opt = input("opt :").lower()
    
















