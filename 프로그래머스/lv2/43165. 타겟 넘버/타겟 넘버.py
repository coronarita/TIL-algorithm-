# Python Sol with bfs
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    
    queue.append((numbers[0], 0))
    queue.append((-numbers[0], 0))
    
    while queue :
        p = queue.popleft()
        if p[1] == len(numbers) -1 :
            if p[0] == target :
                answer += 1
            continue
            
        queue.append((p[0] + numbers[p[1]+1], p[1]+1))
        queue.append((p[0] - numbers[p[1]+1], p[1]+1))
    
    return answer