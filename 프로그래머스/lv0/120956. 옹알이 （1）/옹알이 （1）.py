from itertools import permutations

def solution(babbling):
    answer = 0
    word = []
    available = ["aya", "ye", "woo", "ma"]
    
    for i in range(1, len(available)+1):
        for j in permutations(available, i):
            word.append("".join(j))
    
    print(word)
            
    for b in babbling :
        if b in word :
            answer += 1
            
    return answer