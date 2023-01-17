import re
def solution(my_string):
    answer = sum([int(i) for i in re.sub(r"[a-zA-Z]", " ", my_string).split()])
    # print(re.sub(r"[a-zA-Z]", " ", my_string).split())
    return answer