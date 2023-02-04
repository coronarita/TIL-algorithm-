def solution(s):
    answer = []
    cnt = 0
    turn = 0
    while s != '1' : 
        temp = ''        
        for ch in s :
            # 변환의 횟수
            if ch == '0' : 
                # 제거된 0의 갯수
                cnt += 1
                
            else : 
                temp += ch
                
        # 2진 변환
        s = bin(len(temp))[2:]     
        turn += 1
        
    answer.append(turn)
    answer.append(cnt)
    return answer