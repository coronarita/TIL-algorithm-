def solution(numbers):
    answer = 0
    k_list = sorted(numbers)
    m1 = k_list[0]*k_list[1]
    m2 = k_list[-2]*k_list[-1]
    return max(m1,m2)