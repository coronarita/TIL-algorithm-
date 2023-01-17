def solution(array, n):
    array.sort()
    gap = [abs(i-n) for i in array]
    gap_idx = [i for i in zip(array, gap)]
    return min(gap_idx, key=lambda x : x[1])[0]