def solution(n):
    answer = 0
    for i in range(1, n//2):
        if n / i == i :
            return 1
    return 2