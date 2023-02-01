def solution(n):
    if n == 0 :
        return 0
    else : 
        return sum([i for i in range(1, n+1) if n % i == 0])