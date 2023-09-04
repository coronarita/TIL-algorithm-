import copy
import sys
sys.setrecursionlimit(100000)

# inputs
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# var
ret = 0

# class 로 받게되면 memory 초과가 남
# stack 쓰거나, 메모리 최소화하거나
# init_map = copy.deepcopy(grid)

def rotate(arr):
    temp = [[0]*n for _ in range(n)]

    # rotate cw 90 degree
    for y in range(n):
        for x in range(n):
            temp[y][x] = arr[n-x-1][y]

    # update
    for y in range(n):
        for x in range(n):
            arr[y][x] = temp[y][x]
    return arr

def get_max(arr):
    cur_ret = 0
    for y in range(n):
        for x in range(n):
            cur_ret = max(cur_ret, arr[y][x])
    return cur_ret

def up(arr):
    temp = [[0] * n for _ in range(n)]

    for x in range(n):
        flag = 0
        target = -1
        for y in range(n):
            if arr[y][x] == 0 : continue

            # update
            if flag and arr[y][x] == temp[target][x] :
                flag = 0
                temp[target][x] *= 2
            else :
                flag = 1
                target += 1
                temp[target][x] = arr[y][x]

        target+= 1
        while target < n :
            temp[target][x] = 0
            target += 1

    for y in range(n):
        for x in range(n):
            arr[y][x] = temp[y][x]

    return arr

# def dfs(cur, count):
#     global ret
#     if count == 5 :
#         cur_ret = get_max(cur)
#         if ret < cur_ret:
#             ret = cur_ret
#             return
#
#     for dir in range(4):
#         nxt = copy.deepcopy(cur)
#         nxt = up(nxt)
#         dfs(nxt, count + 1)
#         cur = rotate(cur)
#         # print(nxt, cur)

def dfs(grid):
    global ret
    stack = [(grid, 0)]  # Store the grid state and the depth in a stack

    while stack:
        cur, count = stack.pop()
        if count == 5:
            cur_ret = get_max(cur)
            if ret < cur_ret:
                ret = cur_ret
        else:
            for _ in range(4):
                nxt = [row[:] for row in cur]  # Create a new grid copy
                nxt = up(nxt)
                stack.append((nxt, count + 1))
                cur = rotate(cur)

dfs(grid)

# output
print(ret)

# test
# for _ in range(n):
#     print(*grid[_])
