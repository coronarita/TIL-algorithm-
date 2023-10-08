from collections import deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

def rotate_and_melting(board, len_board, L):
    '''
    Level에 맞게, 회전 및 얼음를 녹인다.
    :param board: ice
    :param len_board: 길이
    :param L: 레벨
    :return: board
    '''

    new_board = [[0] * len_board for _ in range(len_board)]

    # rotate
    r_size = 2 ** L # 격자 크기
    for y in range(0, len_board, r_size):  # 격자 시작 y
        for x in range(0, len_board, r_size): # 격자 시작 x
            for i in range(r_size):
                for j in range(r_size):
                    new_board[y+j][x+r_size-i-1] = board[y+i][x+j]

    board = new_board

    # melt
    melting_list = [] # 녹을 좌표
    for y in range(len_board):
        for x in range(len_board):
            ice_count = 0
            for d in range(len(dy)):
                ny = y + dy[d]
                nx = x + dx[d]

                if nx < 0 or ny <0 or nx >=len_board or ny >=len_board:
                    continue
                elif board[ny][nx] > 0 :
                    ice_count+= 1
            if ice_count < 3 and board[y][x] != 0 :
                melting_list.append((y, x))

    for y, x in melting_list:
        board[y][x] -= 1

    return board

def bfs(board, len_board):

    used = [[False] * len_board for _ in range(len_board)]
    ice_sum = 0
    max_area_count = 0
    for y in range(len_board):
        for x in range(len_board):
            area_count = 0
            if used[y][x] or board[y][x] == 0:
                continue

            q = deque()
            q.append((y, x))
            used[y][x] = True

            while q:
                sy, sx = q.popleft()
                ice_sum += board[sy][sx] # 얼음합 추가
                area_count += 1 # 얼음카운트 추가

                for d in range(4):
                    ny= sy+dy[d]
                    nx = sx+dx[d]
                    if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board or used[ny][nx]:
                        continue
                    if board[ny][nx] != 0 :
                        used[ny][nx] = True
                        q.append((ny, nx))

            max_area_count = max(max_area_count, area_count)

    print(ice_sum)
    print(max_area_count)



def simulate():
    N, Q = tuple(map(int, input().split()))
    grid_size = 2**N
    ice = [list(map(int, input().split())) for _ in range(grid_size)]
    levels = list(map(int, input().split()))

    for L in levels:
        ice = rotate_and_melting(ice, grid_size, L)

    bfs(ice, grid_size)

simulate()