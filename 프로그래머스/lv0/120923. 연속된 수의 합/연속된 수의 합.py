def solution(num, total):
    answer = []
    a_0 = (2*total/num + 1 - num)/2
    
    for i in range(num):
        answer.append(a_0 + i)
    
    
    return answer