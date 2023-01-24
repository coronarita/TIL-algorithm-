def print_board(board) :
    for i in range(len(board[0])) :
        print(board[i])

def check_mine(board, mine):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 :
                mine.append((i, j))
    return mine
            
def check_safe(board):
    num_safe = 0
    for i in range(len(board[0])) :        
        for j in range(len(board[0])):
            if board[i][j] == 0 :
                num_safe += 1
        # print(mine[i])
    return num_safe

def danger(board, x, y) :
    dx = [-1, 1, 0, 0, -1,-1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < N and 0 <= ny < N :
            board[nx][ny] = 1
    return board
        
def solution(board):
    answer = 0
    global N
    N = len(board[0])    
    mine = []
    # # test the shape
    # print_board(board)
    mine = check_mine(board, mine)
    for x,y in mine :
        danger(board,x,y)
    answer = check_safe(board)
    
    return answer
