# def solution(array, n):
#     array.sort() # 진행할 때, 정렬을 하고 진행하는 것이, hidden case 오답을 방지할 수 있다.
#     gap = [abs(i-n) for i in array]
#     gap_idx = [i for i in zip(array, gap)]
#     return min(gap_idx, key=lambda x : x[1])[0]



solution=lambda array,n:sorted(array,key=lambda x:(abs(x-n),x))[0]
