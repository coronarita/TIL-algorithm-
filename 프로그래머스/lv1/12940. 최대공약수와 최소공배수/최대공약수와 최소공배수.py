import math

def solution(n, m):
    answer = []
    answer.append(math.gcd(n,m))
    if math.gcd(n,m) == 1 :
        answer.append(n*m)
    
    else : 
        answer.append(n *m / math.gcd(n,m) )
        
    return answer