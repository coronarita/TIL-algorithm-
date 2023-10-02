DICE = 6
n, m, x, y, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
cmds = list(map(int, input().split()))
dice = [0 for _ in range(DICE+1)]
# manage status of dice
top, front, right = 1, 2, 3
# LEFT 4 REAR 5 BOTTOM 6

def print_output(ismoved):
    global x, y, top, front, right
    if ismoved :
        print(dice[top])
    else :
        return

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

def update(cmd):
    '''
    이동명령(cmd)에 따라 칸에 쓰여진 수가
    0이면
    주사위의 바닥면이 칸에 복사
    0이 아니면
    주사위의 바닥면으로 칸의 수가 복사, 칸은 0으로
    :return: ismoved(flag) - 주사위가 움직인지 여부
    '''
    global x, y, top, front, right
    # 이동
    dxs, dys = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
    nx, ny = x + dxs[cmd], y + dys[cmd]
    if not in_range(nx, ny): return False
    x, y = nx, ny

    # 주사위 회전 필요
    if cmd == 1:
        top, right = 7-right, top
    elif cmd == 2:
        top, right = right, 7-top
    elif cmd == 3 :
        top, front = front, 7-top
    else :
        top, front = 7-front, top
    # print(top, front, right)
    # print(dice)
    # 칸의 수와 비교
    if grid[x][y] == 0 :
        grid[x][y] = dice[7-top]
    else :
        dice[7 - top] = grid[x][y]
        grid[x][y] = 0

    return True


def simulate(cmd):
    '''
    cmd - 육면체의 진행방향
    육면체와, 바닥의 수 상태에 따라 상태가 업데이트 되며,
    결과값이 출력된다.
    :param cmd:
    :return: None
    '''
    global x, y, top, front, right

    ismoved = update(cmd)

    print_output(ismoved)

for cmd in cmds :
    simulate(cmd)