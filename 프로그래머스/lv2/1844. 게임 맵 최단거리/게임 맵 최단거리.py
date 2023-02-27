# direction : U D L R
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps):
    # bfs with queue
    from collections import deque
    
    q = deque()
    q.append((0, 0))
    
    while q : 
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
                
            if maps[nx][ny] == 0 :
                continue    
            
            if maps[nx][ny] == 1 : 
                maps[nx][ny] = maps[x][y]+ 1
                q.append((nx, ny))

    if maps[len(maps)-1][len(maps[0])-1] >= 2:
        return maps[len(maps)-1][len(maps[0])-1]
    return -1

def solution(maps):
    answer = 0   
    return bfs(maps)