# hash 사용해서 풀이

def solution(nums):
    poke = {}
    for n in nums :
        if hash(n) not in poke :
            poke[hash(n)] = 1
        else : 
            poke[hash(n)] += 1

    return min(len(poke.keys()), len(nums)/2)


# 시간초과 코드
# from itertools import combinations

# def solution(nums):  
#     ans = -99999

#     for case in list(combinations(nums, int(len(nums)/2))) :
#         ans = max(ans, len(set(case)))
#     return ans