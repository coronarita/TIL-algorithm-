def solution(a, b):
    answer = 0
    if a > b :
        for i in range(a-b+1):
            answer += b+i
        
    elif a < b : 
        for i in range(b-a+1):
            answer += a+i
        
        
    else : 
        answer = a
        
    return answer