CCW = -1
CW = 1
NO_ROTATE = 0

chairs = [
    list(map(int, input()))
    for _ in range(4)
]

k = int(input())
chairs_rotate = [NO_ROTATE for _ in range(4)]

def flip(i):
    return CW if i == CCW else CCW

def shift(chair_num, directions):
    if directions == CW :
        chairs[chair_num] = chairs[chair_num][-1:] + chairs[chair_num][:-1]

    elif directions == CCW :
        chairs[chair_num] = chairs[chair_num][1:] + chairs[chair_num][:1]

    else :
        return

# print(chairs)

# for loop
for _ in range(k):
    # check rotate chair
    chairs_rotate = [NO_ROTATE for _ in range(4)]

    start_chair, direction = tuple(map(int, input().split()))
    start_chair -= 1

    chairs_rotate[start_chair] = direction

    # left
    for i in range(start_chair-1, -1, -1):
        if chairs[i][2] != chairs[i+1][6] :
            chairs_rotate[i] = flip(chairs_rotate[i+1])
        else : break

    # right
    for i in range(start_chair+1, 4):
        if chairs[i][6] != chairs[i-1][2] :
            chairs_rotate[i] = flip(chairs_rotate[i-1])
        else : break


    # rotate
    for idx, chr in enumerate(chairs_rotate):
        shift(idx, chr)

# print(chairs)
print(sum([
    2 ** i for i in range(4) if chairs[i][0] == 1
]))