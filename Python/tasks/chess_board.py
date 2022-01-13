
def create_board(n):
    board = []
    rows, cols = (n, n)
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append('-')
        board.append(col)
    return board

def display_board(brd):
    r = len(brd) 
    for i in range(r):
        print(brd[i])

def check(brd, active_r, active_c):
    for i in range(n):
        for j in range(n):
            if i == active_r or j == active_c or (active_r - i) == (j - active_c) or (active_r - i) == (active_c - j):
                brd[i][j] = '#'

#n = int(input("Enter a number: "))
n = 8
brd = create_board(n)

active_r, active_c = (0, 0)
check(brd, active_r, active_c)

display_board(brd) 