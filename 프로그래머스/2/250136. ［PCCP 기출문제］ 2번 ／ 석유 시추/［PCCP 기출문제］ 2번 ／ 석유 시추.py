# dfs로 다시풀어보기
def solution(land):
    n, m = len(land), len(land[0])
    oil_cnt = [0] * m
    visited = [[True] * m for _ in range(n)]
    dxs, dys = [0,1,0,-1], [1,0,-1,0]
    
    def in_range(x, y):
        return 0<=x and x<n and 0<=y and y<m
    
    for i in range(n):
        for j in range(m):
            if land[i][j] and visited[i][j] : 
                visited[i][j] = False
                cnt = 0
                col = set()
                s = [(i, j)] # stack for dfs
                while s :
                    x, y = s.pop()
                    cnt += 1
                    col.add(y)
                    
                    for dx, dy in zip(dxs,dys):
                        nx, ny = x+dx, y+dy 
                        if not in_range(nx, ny) : continue
                        if land[nx][ny] and visited[nx][ny] : 
                            visited[nx][ny] = False
                            s.append((nx, ny))
                            
                for y in col :
                    oil_cnt[y] += cnt
    # print(oil_cnt)
    return max(oil_cnt)