from collections import defaultdict

def solution(array):
    answer = defaultdict(int)
    components = list(set(array))
    for arr in array :
        for component in components:
            if arr == component :
                answer[component] += 1
    # print(answer.keys(), answer.values())
    # print(set(answer.keys()), set(answer.values()))
    
    # print(max((answer, key =lambda x: answer[x])))
    # print(max(answer.values())) # <--최빈값 
    rev = defaultdict(list)
    for key, val in answer.items():
        rev[val].append(key) 
        
    print(rev)
    if len(rev[max(answer.values())]) > 1 :
        return -1 
    
    # ###  problem : 중복 요소가 2개인 경우 ... (333 444 22 55 -> 캐치하지 못함)
    # if len(set(answer.values())) == 1 and len(answer.keys()) > 1 :
    #     return -1
        
    answer_reversed = [(val, key) for key, val in answer.items()]
    
    # print(answer_reversed)
    
    return max(answer_reversed, key=lambda x: x[0])[1]