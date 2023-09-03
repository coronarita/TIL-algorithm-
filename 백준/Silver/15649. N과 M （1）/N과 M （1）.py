
n, m = map(int, input().split())

selected = []
numbers = [i + 1 for i in range(n)]
isused = [False for i in range(n+1)]

def recur_num(cnt):
    if cnt == m :
        print(*selected)
        return

    # 중복 사용 안되는데
    for number in numbers :
        if not isused[number]:
            isused[number] = True
            selected.append(number)
            recur_num(cnt + 1)
            selected.pop()
            isused[number] = False
recur_num(0)