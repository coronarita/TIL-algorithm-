def solution(n):
    # 연속된 수니까, 각 수 간의 차가 c로 이루어져 있다고 보고. 
    # 수의 차(누적 c)를 n에서 빼준 값을 수의 차(c)로 나누었을 때 나누어 떨어지면, 이 수는 연속된 자연수들로 표현할 수 있다.
    answer = 0
    c = 0
    n -= c
    
    while n > 0 :
        c += 1
        n -= c
        if n % c == 0 : 
            answer += 1
    
    return answer

    