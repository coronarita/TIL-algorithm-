class rectangle():
    
    def __init__(self, dots):
        self.dots = sorted(dots) # x, y 좌표 계산을 편리하게 하려고
        self.width = abs(self.dots[2][1] - self.dots[1][1])
        self.height = abs(self.dots[2][0] - self.dots[1][0])

    def get_area(self):
        return self.width*self.height
def solution(dots):
    a = rectangle(dots)
    
    return a.get_area()