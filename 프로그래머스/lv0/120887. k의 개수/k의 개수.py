def solution(i, j, k):
    answer = 0
    ans =""
    for a in range(i, j+1) : 
        ans += str(a)
    
    return ans.count(str(k))