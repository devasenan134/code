

def game_score(board):
    display_board(board)
    res = 0


    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            res = 1 if board[0][i] == 'x' else -1
        if board[i][0] == board[i][1] == board[i][2]:
            res = 1 if board[0][i] == 'x' else -1

    if board[0][0] == board[1][1] == board[2][2]:
        res = 1 if board[0][i] == 'x' else -1
    if board[0][2] == board[1][1] == board[2][0]:
        res = 1 if board[0][i] == 'x' else -1
    
    print(res)
    return res


def find_slots(board):
    available = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                available.append((i, j))
    
    return available


            
def minimax(board, maxi, score):
    count = 0
    tot_score = 0
    available = find_slots(board)

    if len(available) == 0:
        return game_score(board), (-1, -1)

    if maxi:
        score = -999999999
        for i, j in available:
            # print(slot[0], slot[1])
            board[i][j] = 'x'
            new_score, slot = minimax(board, False, score)
            tot_score += new_score
            count += 1 
            if new_score > score:
                score = new_score
                slot = (i, j)
            board[i][j] = ' '

    
    else:
        score = 999999999
        for i, j in available:
            # print(slot[0], slot[1]) 
            board[i][j] = 'o'
            new_score, slot = minimax(board, True, score)
            tot_score += new_score
            count += 1
            if new_score < score:
                score = new_score
                slot = (i, j)
            board[i][j] = ' '

    return tot_score/count, slot


def define_board():
    board = [['x', ' ', ' '],
             ['o', 'o', ' '],
             ['x', 'x', 'o']]

    return board


def display_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j] + "  ", end="")
        print()
    print()





board = define_board()
display_board(board)

print(minimax(board, True, 0, 1))
