import sys
# sys.setrecursionlimit(100000)

n, s = tuple(map(int, input().split()))
integers = sorted(list(map(int, input().split())))
ans = 0
selected = []

def backtracking(cnt):
    global ans

    # 종료 조건
    if cnt == n :
        if selected and sum(selected) == s:  # 공집합이 아닌 경우만 확인
            ans += 1
        return

    selected.append(integers[cnt])
    backtracking(cnt + 1)
    selected.pop()
    backtracking(cnt + 1)

backtracking(0)
print(ans)  # -1을 빼는 부분을 제거
