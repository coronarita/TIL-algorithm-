def gap(char):
    if ord(char) >= ord('N') : 
        return ord('[') - ord(char)
    else : 
        return ord(char) - 65

def solution(name):
    answer = 0

    # 'JEROEN'
    min_move = len(name) - 1

    # 1. for changing each characters
    for idx, char in enumerate(name) :  
        # difference from 'AAAA'
        
        answer += gap(char)
        #move left

        # 2. need to count moving    
        # find pos with serialized 'A'
        next_pos = idx + 1
        while next_pos < len(name) and name[next_pos] == 'A':
            next_pos += 1
        print(next_pos)
        min_move = min([min_move,                         
                        2*idx + len(name) - next_pos,
                       idx + 2*(len(name) - next_pos)])  #straight, left, right
    
    answer += min_move
    return answer
