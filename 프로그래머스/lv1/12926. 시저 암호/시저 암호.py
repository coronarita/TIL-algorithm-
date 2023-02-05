def solution(s, n):
    answer = ''
    #shifting algorithm
    
    for i in range(len(s)):
        if s[i] != " " : 
            ans  = ord(s[i])+n
            if s[i].isupper(): # capital
                if ans > 90 : 
                    answer += chr(ans-26)
                else : 
                    answer += chr(ans)
            else :  # lower
                if ans > 122:
                    answer += chr(ans-26)
                else : 
                    answer += chr(ans)
            
        else : 
            answer += " "
    return answer