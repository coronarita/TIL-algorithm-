# Stack을 활용해서 풀어야, 시간, 효용성 모두 만족 가능! 

def solution(s):
    stack = []
    
    for c in s :
        if len(stack) == 0 :
            stack.append(c)
        else :
            if stack[-1] == c :
                stack.pop()
            else :
                stack.append(c)
    if len(stack) == 0:
        return 1
    return 0


'''
time out 발생
'''
# def solution(s):
#     while len(s) != 0 :
#         flag = 0
#         for idx in range(len(s)-1):
#             if s[idx] == s[idx+1] : 
#                 s = s[:idx] + s[idx+2:]
#                 flag = 1
#                 break
#         if flag == 0 :
#             break
            
#     if len(s) == 0 : 
#         return 1
#     return 0