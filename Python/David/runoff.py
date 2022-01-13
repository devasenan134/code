def runoff():
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
        print()        
        for j in range(3) :
            voter = input(f"Rank {j+1}: ")
            if j == 0 :
                candidates[voter] += 3
            elif j == 1 :
                candidates[voter] += 2
            elif j == 2 :
                candidates[voter] += 1
    # print(candidates)
    highest = max(candidates.values())
    for key, value in candidates.items() :
        if highest == value :
            print(key)
    
opt = "y"
while opt == "y" :
    runoff()
    opt = input("opt: ").lower()
