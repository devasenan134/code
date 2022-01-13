def minion_game(string):
    l = len(string)

    vowels = ["A", "E", "I", "O", "U"]
    stuart_words = []
    kevin_words = []

    s_pts = {}
    k_pts = {}
    s_score = 0
    k_score = 0

    for s in range(l):
        if string[s] not in vowels:
            for i in range(s, l):
                stuart_words.append(string[s:i+1])
        else:
            for j in range(s, l):
                kevin_words.append(string[s:j+1])
    
    for word in stuart_words:
        if word not in s_pts:
            s_pts[word] = 1
        else:
            s_pts[word] += 1

    for word in kevin_words:
        if word not in k_pts:
            k_pts[word] = 1
        else:
            k_pts[word] += 1

    for score in s_pts:
        s_score += s_pts[score]
    for score in k_pts:
        k_score += k_pts[score]

    if s_score > k_score:
        print("Stuart", s_score)
    elif k_score > s_score:
        print("Kevin", k_score)    
    else:
        print("Draw")
    

s = input(">>")
minion_game(s)
