#review

from collections import deque

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    
    while queue :
        n = queue.popleft()
        for g in graph[n]:
            if visited[g] == 0 :
                visited[g] = visited[n] + 1
                queue.append(g)
    
    return max(visited)

def solution(n, vertex):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for v in vertex :
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])
    
    for g in graph : 
        g.sort()
    # print(graph)
    visited = [0] * (n+1)
    visited[1] = 1
    m = bfs(graph, 1, visited)
    
    return visited.count(m)