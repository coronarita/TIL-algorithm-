n, s = tuple(map(int, input().split()))
integers = sorted(list(map(int, input().split())))
ans = 0

def backtracking(cnt, total):
    global ans

    # 종료 조건
    if cnt == n:
        if total == s:
            ans += 1
        return

    # 현재 원소를 포함하는 경우
    backtracking(cnt + 1, total + integers[cnt])
    
    # 현재 원소를 포함하지 않는 경우
    backtracking(cnt + 1, total)

backtracking(0, 0)
if s == 0:  # 합이 0인 경우 공집합도 카운트될 수 있으므로 1을 빼줍니다.
    ans -= 1
print(ans)
