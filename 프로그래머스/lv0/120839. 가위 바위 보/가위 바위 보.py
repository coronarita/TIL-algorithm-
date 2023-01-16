def solution(rsp):
    # 2 0 5 2 0 5
    answer = ''
    for turn in rsp :
        if turn == "2":
            answer += "0"
        elif turn == "0":
            answer += "5"
        else : 
            answer += "2"
    return answer