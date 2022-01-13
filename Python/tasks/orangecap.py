def Orangecap(d):
    dics = d.values()
    high_s = 0
    hitter = ''
    total_s = 0
    for dic in dics:
        players = list(dic.keys())
        scores = list(dic.values())
        for score in scores:
            if score >= high_s:
                high_s = score
        for player in players:
            if dic[player] == high_s:
                hitter = player

    for dic in dics:
        s = dic.get(hitter)
        if s:
            total_s += s
    return hitter, high_s, total_s
    


d = {'test1':{'Dhoni':74, 'Kohli':15},
   'test2':{'Dhoni':29, 'Pujara':42}
   }

player, high_score, total_score = Orangecap(d)
print(f"The player with highest score is {player} and the total score of {player} is {total_score}")
