def plurality():
    candidates = dict()
    candidates_list = input("candidates: ").split()
    for candidate in candidates_list :
        if candidate not in candidates :
            candidates[candidate] = 0
        else :
            continue
    # print(candidates)
    voter = ""
    no = int(input("Number of voters: "))
    for i in range(no) :
        voter = input("Vote: ")
        if voter in candidates :
             candidates[voter] += 1
        else :
            continue
    highest = max(candidates.values())
    for key, value in candidates.items() :
        if highest == value :
            print(key)
    
opt = "y"
while opt == "y" :
    plurality()
    opt = input("opt: ").lower()
