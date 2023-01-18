def solution(balls, share):
    nom = 1
    denom = 1
    for i in range(balls, balls - share , -1):
        nom *= i

    for i in range(share, 0, -1):
        denom *= i
    
    return nom / denom
'''
4가지의 test case에서 timeout이 나왔음! 

from itertools import combinations 

def solution(balls, share):
    ball = [i for i in range(balls)]
    a = list(combinations(ball, share))
    return len(a)
'''
