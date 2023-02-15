def solution(sizes):
    # 1. w, h를 [긴변, 작은변] 으로 정렬
    new_sizes = []
    for size in sizes :
        w, h = size[0], size[1]
        if h>= w :
            w, h = h, w
        new_sizes.append([w,h])
    
    # 2. w, h에서 최댓값 추출
    max_w, max_h = 0, 0
    for new_size in new_sizes: 
        w, h = new_size[0], new_size[1]
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    
    # 3. Area = w x h     
    return max_w * max_h