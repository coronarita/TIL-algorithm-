def solution(order):
    return len([o for o in str(order) if int(o)%3 == 0 and int(o)!=0])