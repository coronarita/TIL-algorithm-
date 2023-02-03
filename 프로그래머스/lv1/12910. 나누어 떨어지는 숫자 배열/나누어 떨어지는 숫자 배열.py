def solution(arr, divisor):
    result = []
    for num in sorted(arr) : 
        if num%divisor == 0 :
            result.append(num) 
    
    if len(result) == 0 : 
        return [-1]
    
    return result