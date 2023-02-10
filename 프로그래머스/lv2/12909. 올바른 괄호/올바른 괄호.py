from collections import deque
def solution(s):
    q = deque(s)
    cnt = 0
    while(q):
        if q.popleft() == "(":
            cnt += 1
        else : cnt -= 1
        
        if cnt < 0 : 
            return False
            break   
    if cnt > 0:
        return False
    
    return True

# 정확성 만점 , 효용성 0점
# def solution(s):
    
#     for i in range(len(s)//2) : 
#         if "()" in s :
#             s = s.replace("()", "")
            
#     return False if len(s) != 0 else True