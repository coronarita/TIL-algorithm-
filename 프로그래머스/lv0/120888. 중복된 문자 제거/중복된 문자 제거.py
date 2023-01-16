from collections import defaultdict

def solution(my_string):
    answer = ''
    s_list = defaultdict()
    for my_str in my_string :
        s_list[my_str] = 1
        
    return ''.join([*s_list.keys()])