n, m, t = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
vacuum = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == -1]

# Debug
def printgrid():
    for _ in range(n):
        print(*grid[_])
    print()

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

def spread():

    temp = [[0] * m for _ in range(n)]
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    for x in range(n):
        for y in range(m):
            if grid[x][y] == -1 : continue
            target = grid[x][y]
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if not in_range(nx, ny) or grid[nx][ny] == -1 : continue
                # 확산해서 더해줘야 함
                val = target//5
                temp[nx][ny] += val
                grid[x][y] -= val

    for x in range(n):
        for y in range(m):
            grid[x][y] += temp[x][y]

def rotate_upward():
    s_x, s_y = vacuum[0]

    # rotate counterclockwise
    ## left-edge
    for x in range(s_x, 0, -1):
        if x == s_x : continue
        grid[x][s_y] = grid[x-1][s_y]
    ## upper-edge
    for y in range(m-1):
        grid[0][y] = grid[0][y+1]
    ## right-edge
    for x in range(s_x):
        grid[x][m-1] = grid[x+1][m-1]
    ## lower-edge
    for y in range(m-1, 0, -1):
        if y == s_y + 1 :
            grid[s_x][y] = 0
            continue

        grid[s_x][y] = grid[s_x][y-1]


def rotate_downward():
    s_x, s_y = vacuum[1]

    # rotate clockwise
    ## left-edge
    for x in range(s_x, n-1):
        if x == s_x : continue
        grid[x][s_y] = grid[x + 1][s_y]
    ## lower-edge
    for y in range(m - 1):
        grid[n-1][y] = grid[n-1][y+1]
    ## right-edge
    for x in range(n-1, s_x, -1):
        grid[x][m-1] = grid[x - 1][m-1]
    ## upper-edge
    for y in range(m - 1, 0, -1):
        if y == s_y + 1:
            grid[s_x][y] = 0
            continue
        grid[s_x][y] = grid[s_x][y - 1]

    # printgrid()

def simulate():

    # 1. spread
    spread()

    # 2. rotate upward - CCW /downward - CW
    rotate_upward()
    rotate_downward()

for _ in range(t):
    simulate()

# ans
print(sum([
    sum(grid[i]) for i in range(n)
    ])+2)



