def solution(x):
    answer = True
    dig = 0
    for i in str(x):
        dig += int(i)
    
    if x % dig != 0:
        answer = False
    
    return answer