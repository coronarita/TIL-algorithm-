def solution(num):
    answer = 0
    count = 0
    while num >1 :
        print(num)
        if num % 2 == 0 : 
            num //= 2 
            count += 1
        else : 
            num = num*3 + 1 
            count += 1 
        
        if count >500 and num != 1 :
            return -1
    
    return count