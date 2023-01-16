def fact(num):
    if num == 1 :
        return 1
    else : 
        return num* fact(num-1)
        
def solution(n):
    answer = 0
    for i in range(1, 11):
        if fact(i) == n :
            return i
        elif fact(i) > n: 
            return i-1