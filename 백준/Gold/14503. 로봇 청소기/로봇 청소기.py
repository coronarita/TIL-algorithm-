n, m = tuple(map(int, input().split()))
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

x, y, d = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited[x][y] = True
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

def simulate():
    global x, y, d
    flag = True
    cnt = 0
    while flag :
        # 1. 현재 방향 기준, 왼쪽 방향 1번도 간 적이 없다면
        nd = (d-1) % 4
        nx, ny = x + dxs[nd], y + dys[nd]
        # 좌회전 + 1칸 전진
        if not visited[nx][ny] and grid[nx][ny] == 0 :
            visited[nx][ny] = True
            x, y = nx, ny
            d = nd
            cnt = 0

        # 2. 왼쪽 방향이 인도 혹은 이미 방문
        elif visited[nx][ny] or grid[nx][ny] == 1 :
            d = nd
            # 좌회전 + 1번으로
            cnt += 1

        # 3. 4방향 모두 돌았는데, 전진이 불가능하다면
        if cnt == 4 :
            # 방향 유지, 후진 + 1번으로
            nx, ny = x - dxs[nd], y - dys[nd]
            x, y = nx, ny
            cnt = 0

        # 4. 3번까지도 불가 (뒤가 인도) -> Stop
        if grid[x][y] == 1 :
            flag = False
        # print(x, y, d)

simulate()
print(sum([1 for i in range(n) for j in range(m) if visited[i][j]]))