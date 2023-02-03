def solution(s):
    answer = ''
    
    temp = map(int, s.split())
    answer += str(min(temp))
    answer += ' '
    temp = map(int, s.split())
    answer += str(max(temp))
    
    return answer