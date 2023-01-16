def solution(numer1, denom1, numer2, denom2) : 
    numer = numer1*denom2 + numer2*denom1
    denom = denom1*denom2
    div = []
    # 약분이 가능한지 판단 (최대공약수 2 이상이면)
    for i in range(2, numer+1):
        if numer % i == 0 and denom % i == 0 :
            div.append(i)

    if div : 
        return [numer/max(div), denom/max(div)]
    else : return [numer, denom]