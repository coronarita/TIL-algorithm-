def solution(s):
    answer = 0
    op_list = s.split()
    print(op_list)
    
    for idx, op in enumerate(op_list) : 
        if op == 'Z':
            answer -= int(op_list[idx-1])
        else : 
            answer += int(op)
        
        
    return answer