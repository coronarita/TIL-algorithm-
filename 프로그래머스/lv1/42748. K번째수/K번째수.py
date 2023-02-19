def solution(array, commands):
    answer = []
    
    for command in commands : 
        # command[0], command[1] - starts(n+1), end(n+1) 
        # command[2], n+1th number
        
        answer.append(sorted(array[command[0]-1:command[1]])[command[2]-1])
    
    
    return answer