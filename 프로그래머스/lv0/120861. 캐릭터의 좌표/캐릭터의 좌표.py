def solution(keyinput, board):
    
    hor, vert = board[0], board[1]
    x, y = 0, 0
    key_move = {'up' : (0,1), 'down': (0, -1), 'left': (-1, 0), 'right': (1,0)}

    for key in keyinput :
        nx = x + key_move[key][0]
        ny = y + key_move[key][1]
        if abs(nx) <= (hor-1)/2 and abs(ny) <= (vert-1)/2 :
            x, y = nx, ny
        
            
    return [x, y]