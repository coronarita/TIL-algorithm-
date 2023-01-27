from heapq import *
def solution(dots):
    answer = 0
    heapify(dots)
    
    a = heappop(dots)
    b = heappop(dots)
    
    c = heappop(dots)
    d = heappop(dots)
    
    # gradient  calculation
    
    g1 = (b[1]-a[1]) / (b[0]-a[0])
    g2 = (d[1]-c[1]) / (d[0]-c[0])
    
    if g1 == g2 : return 1
    else : return 0