class line():
    def __init__(self):
        self.result = 0
    
    def check_cross(self, a, b):
        l1s, l1e = a[0], a[1]
        l2s, l2e = b[0], b[1]
        max_start = max(a[0], b[0])
        min_end = min(a[1], b[1])
        # print(max_start, min_end, max_start-min_end)
        
        if min_end > max_start :
            self.result += min_end - max_start
        
    def check_triple(self, a,b,c):
        l1s, l2s, l3s = a[0], b[0], c[0]
        l1e, l2e, l3e = a[1], b[1], c[1]
        max_start = max(a[0], b[0], c[0])
        min_end = min(a[1], b[1], c[1])
        # print(max_start, min_end, max_start-min_end)
        if min_end > max_start :
            self.result -= min_end - max_start

def solution(lines):
    answer = 0
    a = line()
    x, y, z = lines
    a.check_cross(x,y)
    a.check_cross(y,z)
    a.check_cross(z,x)
    a.check_triple(x,y,z)
    a.check_triple(x,y,z)
    return a.result

