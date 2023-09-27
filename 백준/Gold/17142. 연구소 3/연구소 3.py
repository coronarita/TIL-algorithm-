from collections import deque

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
if all(grid[i][j] == 2 for i in range(n) for j in range(n)) :
    print(0)
    exit()

hospitals = [
    (i, j) for i in range(n) for j in range(n) if grid[i][j] == 2
]
selected = []
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

track = [
    [-1 for _ in range(n)]
    for _ in range(n)
]
bfs_q = deque()


def init():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            track[i][j] = -1

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def can_go(x,y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] != 1


def bfs():
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    while bfs_q :
        x, y = bfs_q.popleft()
        val = track[x][y]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited[nx][ny] = True
                track[nx][ny] = val + 1
                bfs_q.append((nx, ny))

def calc():

    init()

    for idx in selected :
        i, j = hospitals[idx]
        visited[i][j] = True
        track[i][j] = 0
        bfs_q.append((i,j))

    bfs()
    # for _ in range(n):
    #     print(*track[_])

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0 and track[i][j] == -1 and not visited[i][j] :
                return 9999

    k = max([track[i][j] for i in range(n) for j in range(n) if grid[i][j] != 2])
    if k == -1 :
        return 0
    return k

def backtracking(cnt, start):
    global min_time
    if cnt == m :
        # print(selected) # selected idx
        min_time = min(min_time, calc())
        return

    for idx in range(start, len(hospitals)):
        selected.append(idx)
        backtracking(cnt+1, idx+1)
        selected.pop()

min_time = 9999
backtracking(0, 0)

if min_time == 9999 :
    print(-1)
else :
    print(min_time)