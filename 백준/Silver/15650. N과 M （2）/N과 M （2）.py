n, m = map(int, input().split())
arr = [i + 1 for i in range(n)]
result = []

def combination(cnt, start):
    if cnt == m :
        print(*result)
        return

    for idx in range(start, n):
        result.append(arr[idx])
        combination(cnt + 1, idx + 1)
        result.pop()

combination(0, 0)

