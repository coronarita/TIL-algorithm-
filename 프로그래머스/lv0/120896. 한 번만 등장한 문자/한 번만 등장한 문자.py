from collections import defaultdict
def solution(s):
    answer = ''
    # 등장하는 문자를 뽑아서
    # 한번 - count
    cnt = defaultdict(int)
    for char in s :
        for c_list in list(set(s)) : 
            if char == c_list : 
                cnt[c_list] += 1
                
    
    return ''.join(sorted( [key for key, val in cnt.items() if val == 1]))