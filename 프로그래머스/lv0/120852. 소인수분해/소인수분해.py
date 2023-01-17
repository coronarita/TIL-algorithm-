def isPrime(num):
    for i in range(2, num//2+1):
        if num %i == 0:
            return False
    return True
        
    
def solution(n):
    div = []
    answer = []
    
    # 약수 구하기
    for i in range(2, n+1):
        if n % i == 0 :
            div.append(i)
    # 약수 중 소수 찾기
    for ans in div :
        if isPrime(ans) : 
            answer.append(ans)
        
    return answer

