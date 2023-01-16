def solution(hp):
    answer = 0
    army = [5, 3, 1]
    for arm in army : 
        if hp >= arm :
            answer += hp // arm
            hp = hp % arm            
    
    return answer