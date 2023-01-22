import math

def sosu(n):
    # 소수 판별
    for i in range(2, n//2+1):
        if n%i == 0 :
            return False
    return True

def solution(a, b):
    answer = 0
    
    # 기약분수 변환
    gcd = math.gcd(a, b)
    if a % gcd == 0 and b % gcd == 0:
        a //= gcd
        b //= gcd
        
    # 분모의 소인수 판별
    soinsu = []
    for i in range(3, b+1):
        if sosu(i):
            soinsu.append(i)
    if 5 in soinsu : 
        soinsu.remove(5)
    print(soinsu)
    for su in soinsu : 
        if b % su == 0 : 
            return 2
    
    return 1