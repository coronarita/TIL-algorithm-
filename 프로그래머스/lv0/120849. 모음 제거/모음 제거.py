def solution(my_string):
    p_list = ['a', 'e', 'i', 'o', 'u']
    for s in p_list :
        if s in my_string : 
            my_string = my_string.replace(s, "")
    return my_string