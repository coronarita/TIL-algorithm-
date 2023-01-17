def solution(num_list, n):
    ans = []
    col = len(num_list)//n
    for i in range(col):
        ans.append(num_list[n*i:n*(i+1)])
        
    return ans