def solution(n):
    k = n+1
    while str(bin(n)[2:]).count('1') != str(bin(k)[2:]).count('1') : 
        k += 1 
    
    return k

