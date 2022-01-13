def substitution() :    
    string = input("plaintext: ")
    while True :
        substitution = input("substitution: ")
        n = len(substitution)
        if n < 26 :
            print("Key must contain exactly 26 characters.")
            continue
        else :
            break
    cipher = ''
    alphau = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphal = "abcdefghijklmnopqrstuvwxyz"
    for s in string :
            if s not in alphal and s not in alphau :
                cipher += s
            elif s.islower() :
                cipher += substitution[alphal.find(s)].lower()
            elif s.isupper() :
                cipher += substitution[alphau.find(s)].upper()

    print(cipher)

opt = "y"
while opt == "y" :
    substitution()
    opt = input("opt: ").lower()
    
