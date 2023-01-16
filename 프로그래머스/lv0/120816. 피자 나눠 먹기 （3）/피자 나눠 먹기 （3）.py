def solution(slice, n):   
    
    res = 1
    while 1 : 
        if slice * res >= n :
            break
        else :
            res += 1
    return res