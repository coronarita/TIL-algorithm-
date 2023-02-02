def solution(x, n):
    answer = []
    for num in range(n):
        answer.append(x*(num+1))
    return answer