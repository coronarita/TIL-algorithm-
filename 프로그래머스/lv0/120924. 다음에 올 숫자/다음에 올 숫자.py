def solution(common):
    gap = []
    gap2 = []
    for n in range(0, 2) : 
        gap.append(common[n+1] - common[n]) 
        if common[n] != 0 : 
            gap2.append(common[n+1]//common[n])     
        else : 
            continue
        
    # 등차 여부 판단
    if len(set(gap)) == 1 :
        return common[-1] + gap[0]
    
    # 등비 여부 판단
    else :
        return common[-1] * gap2[0]