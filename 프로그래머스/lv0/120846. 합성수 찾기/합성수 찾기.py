def prime(x):
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    return True

def solution(n):
    return len([i for i in range(1, n+1) if not prime(i)])

