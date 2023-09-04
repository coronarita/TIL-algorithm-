n, m = tuple(map(int, input().split()))
numbers = sorted(list(map(int, input().split())))
selected = []
final_set = set()
visited = [False] * (n+1)

def pick(cnt):
    if cnt == m :
        final_set.add(tuple(selected))
        return

    for idx in range(n):
        if not visited[idx] :
            selected.append(numbers[idx])
            visited[idx] = True
            pick(cnt+1)
            selected.pop()
            visited[idx] = False
pick(0)
sorted_final = sorted(final_set)
for seq in sorted_final:
    print(*seq)
