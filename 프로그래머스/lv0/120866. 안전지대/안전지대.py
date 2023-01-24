def print_board(board) :
    for i in range(len(board[0])) :
        print(board[i])

def check_mine(board, mine):
    num_mine = 0
    for i in range(len(board[0])) :        
        for j in range(len(board[0])):
            print(mine[i],i, j)
            if board[i][j] == 1 :
                print("mine")
                
                mine[i][j] = 1 
                print(i,j)
        # print(mine[i])
        
    return num_mine, mine

    
def solution(board):
    answer = 0
    mine = [[0] * len(board[0])]*len(board[0])    
    print(board[3][2])
    # # test the shape
    # print_board(board)
    
    ans, mine = check_mine(board, mine)
    # print_board(mine)
    return answer