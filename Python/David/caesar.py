def caesar() :    
    string = input("plaintext: ")
    n = int(input("caesar: "))
    cipher = ''
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * n
    for s in string :
            if s not in alpha :
                cipher += s
            elif s.islower() :
                cipher += alpha[alpha.find(s) + n].lower()
            elif s.isupper() :
                cipher += alpha[alpha.find(s) + n].upper()

    print(cipher)

opt = "y"
while opt == "y" :
    caesar()
    opt = input("opt: ").lower()
    
