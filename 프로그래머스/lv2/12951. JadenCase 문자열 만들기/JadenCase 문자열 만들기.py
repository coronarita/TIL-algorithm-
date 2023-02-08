# 핵심 : 공백문자가 연속으로 나올 경우 공백도 줄임 없이 살아있어어함.
# 1. Str - Capitalize 내장함수 사용 시 첫글자만 대문자로 변경! 

def solution(s):
    res = []
    s = s.split(" ") # 공백문자가 연속해서 나올 경우를 고려 
    
    for word in s : 
        res.append(word.capitalize()) # ['For', '', 'The', '', 'Last', '', 'Week']
    
    return " ".join(res)