def dfs(i, visited, n, computers):
    from collections import deque
    visited[i] = 1
    for j in range(n):
        if i!=j and computers[i][j] == 1:
            if visited[j] == 0:
                dfs(j, visited, n, computers)


def solution(n, computers):
    # initialize
    answer = 0
    visited = [0] * n
    
    # dfs for all nodes
    for i in range(n):
        if visited[i] == 0 :
            dfs(i, visited, n, computers)
            answer += 1
    
    return answer