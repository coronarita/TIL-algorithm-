def solution(d, budget):
    tot, cnt = 0, 0
    d.sort()
    for d_c in d :
        tot += d_c
        if tot <= budget :
            cnt +=1
    
    return cnt