def solution(age):
    answer = ''
    # ord('a') = 97
    for s in str(age):
        answer += chr(97+int(s))
    return answer