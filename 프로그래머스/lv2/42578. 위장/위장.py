### 다시볼 문제 (1회) ###

def solution(clothes):
    answer = 1
    clothHash = {}
    
    for cloth_name, cloth_type in clothes :
        # get을 사용하면 초기화와 동시에 연산이 가능
        # print(clothHash.get(cloth_type))
        
        clothHash[cloth_type] = clothHash.get(cloth_type, 0) + 1
        
    print(clothHash)
    
    # 경우의 수 계산 시 곱하기 ! 머리로는 잘 하는데 구현하려니 아직은 약하다.
    for t in clothHash.keys():
        answer *= (clothHash[t] + 1)
        
    return answer - 1