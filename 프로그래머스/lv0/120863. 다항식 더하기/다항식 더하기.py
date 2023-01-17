def solution(polynomial):
    answer = ''
    
    temp_list = polynomial.replace("+", "").split()
    a, b = 0, 0
    print(temp_list)
    for temp in temp_list :
        # 1이 아닌 x항 연산
        print(a)
        if temp.count('x') == 1 and temp[0]!='x':   
            print(temp.count('x'))
            a += int(temp[:-1])
            
        elif temp == 'x' : 
            a += 1
            
        # 상수항
        else :
            b += int(temp)
    print(a,b)
    
    if a != 0 and b!= 0:
        if a != 1 :
            return f'{a}x + {b}'
        else : 
            return f'x + {b}'
    elif a!= 0 and b == 0:
        if a != 1 :
            return f'{a}x'
        else : 
            return 'x'
    elif a== 0 and b != 0:
        return f'{b}'
    else : 
        return "0"