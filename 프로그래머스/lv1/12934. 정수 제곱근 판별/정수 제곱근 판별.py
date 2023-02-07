# T13만 예외적으로 오류가 나는데, 이유가 뭘까 ? (0.02로 짧은 시간, 따라서 경계조건에 해당할 것으로 판단되는데..)
# return을 else로 if 의 맞대응으로 집어넣으니, T13은 clear, 나머지 대부분에서 break 효과 발생(Error)
# 2,3,5,6,7 식으로 제곱이 아닌 작은 수 부터 테스트케이스로 삽입 --> 5일때 -1이 나와야하는데 9가 나옴! (T13...?)

import math

def solution(n):
    # n = 5
    for i in range(1, int(math.sqrt(n))+1):
        # if n // i == i :
        if n == i**2 :
            return pow(i+1, 2)
            break
            
    else : 
        return -1