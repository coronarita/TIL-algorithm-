def solution(score):
    score_sum = [x[0]+x[1] for x in score]
    score_sorted = sorted(score_sum, reverse = True)
    result = []
    
    # print(score_sorted)
    for score in score_sum:
        # If the values are same, the indices are same.
        # print(score_sorted.index(score))
        
        result.append(score_sorted.index(score)+ 1)
    
    return result
    
    
'''
    score_sum = [x[0]+x[1] for x in score]
    # 순위 매기기를 위한 정렬
    score_sum_sort = sorted([(idx+1, val) for idx, val in enumerate(score_sum)], key = lambda x : x[1], reverse = True)
    print(score_sum_sort)
    
    result = {}
    # print(sorted(score_sum, reverse=True))

    for idx, val in enumerate(score_sum_sort, start = 1) : 
        print(idx, val[1])
        if val[1] not in result :
            result[val[1]] = idx
    print(result)
    
    return [result[val] for val in score_sum]
'''    
