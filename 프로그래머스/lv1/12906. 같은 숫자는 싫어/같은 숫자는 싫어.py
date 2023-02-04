def solution(arr):
    
    res = []
    res.append(arr[0])
    
    for idx, val in enumerate(arr[1:], start = 1):
        if arr[idx] != arr[idx-1]:
            res.append(arr[idx])
        
    return res
    