def solution(emergency):
    em_sort = sorted(emergency, reverse=True)
    
    result = []
    for num in emergency :
        for idx, val in enumerate(em_sort):
            if num == val : result.append(idx+1)
    return result
        
    