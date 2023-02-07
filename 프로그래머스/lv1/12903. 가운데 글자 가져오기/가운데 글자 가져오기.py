def solution(s):
    answer = ''
    if len(s) % 2 != 0 : # 5 - 짝수개
        answer += s[len(s)//2]
    
    else : # 4 - 홀수개
        answer += s[len(s)//2-1:len(s)//2+1]
    
    return answer