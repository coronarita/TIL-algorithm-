def three(n):
    res = ""
    while n != 0 :
        res = str(n % 3) + res
        n = n // 3
    return res


def ten(n):
    res = 0
    for i in range(len(n)):
        res += int(n[-(i+1)]) * pow(3, i)
    return res
    
    
def solution(n):
    answer = 0
    a = three(n)
    a = a[::-1]
    answer = ten(a)    
    return answer

