

def solution(priorities, location):
    answer = 0
    loc_priorities = []
    
    for idx, priority in enumerate(priorities) :
        loc_priorities.append([priority, idx])
        
    # loc_priorities.sort(key =lambda x: x[0], reverse = True) # 순서를 회전시켜야 해서 이렇게 불가능함.
    # print(loc_priorities)
    while loc_priorities :
        tmp = loc_priorities.pop(0)
        if loc_priorities and tmp[0] < max(loc_priorities)[0]:
            loc_priorities.append(tmp)
        else : 
            answer += 1
            if tmp[1] == location :        
                break
    
    return answer