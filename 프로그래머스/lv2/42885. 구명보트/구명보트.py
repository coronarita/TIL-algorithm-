# using two pointers

def solution(people, limit):
    answer = 0 
    people.sort()
    l, r = 0, len(people) - 1

    while l <= r :
        if people[l] + people[r] > limit :
            pass
        else : 
            l += 1
            
        answer += 1
        r -= 1
    
    return answer