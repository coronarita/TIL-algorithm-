def solution(n,a,b):
    answer = 0

    if a > b :
        a, b = b, a
    
    for i in range(n):
        if 2**i >= a :
            expA = i
            break
    for i in range(expA, n):
        if 2**i >= b :
            expB = i
            break
    print(expA, expB)
    if expA == expB :
        num = 2**(expA-1)
        print(num)
        solution(n,a,b)
    else : 
        return expB
    
    return answer