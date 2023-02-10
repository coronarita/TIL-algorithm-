def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    total = 0
    
    for i,j in zip(A,B):
        total += i*j    
        
    return total