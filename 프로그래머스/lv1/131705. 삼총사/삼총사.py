from itertools import combinations

def solution(number):
    answer = 0

    for j in list(combinations(number, 3)) : 
        if sum(j) == 0 :
            print(j)
            answer += 1
    return answer
    