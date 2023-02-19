''' using queue'''

from collections import deque 

def solution(people, limit) :
    answer = 0
    people.sort()
    dq = deque(people)
    
    while dq : 
        if dq[0] + dq[-1] <= limit :
            dq.popleft()
        answer += 1
        if not dq :
            break
            
        dq.pop()
        
        
    return answer









# # using two pointers

# def solution(people, limit):
#     answer = 0 
#     people.sort()
#     l, r = 0, len(people) - 1

#     while l <= r :
#         if people[l] + people[r] > limit :
#             pass
#         else : 
#             l += 1
            
#         answer += 1
#         r -= 1
    
#     return answer