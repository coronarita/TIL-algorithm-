import math

def sosu(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
        else : continue
    return True

def solution(n):
    answer = 0
    
    for i in range(2, n+1):
        if sosu(i):
            answer += 1
        
    return answer