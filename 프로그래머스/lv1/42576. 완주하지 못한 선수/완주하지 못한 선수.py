
# set 으로 풀이하면 동명이인을 캐치하지 못한다..!

##### 다시 볼 문제 (2/9 기준) ####
# 1. sort / for loop 활용

# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
    
#     for i in range(len(completion)):
#         if participant[i] != completion[i] : 
#             return participant[i]
    
#     return participant[len(participant)-1]

# 2. Hash

# def solution(participant, completion):
#     hashDict = {}
#     hashSum = 0
    
#     for part in participant : 
#         hashDict[hash(part)] = part
#         hashSum += hash(part)
    
#     for comp in completion :
#         hashSum -= hash(comp)
        
#     return hashDict[hashSum]

# 3. Counter
from collections import Counter

def solution(participant, completion):
    a = Counter(participant)
    b = Counter(completion)
    return list(a-b)[0]