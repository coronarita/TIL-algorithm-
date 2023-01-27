class serviceChicken():
    def __init__(self, chicken):
        self.chicken = chicken
        self.coupon = chicken
        self.s_chicken = 0
        
    def get_chicken(self) :
        # 10마리당 서비스치킨 하나
        self.s_chicken += self.coupon // 10
        # 1마리는 쿠폰이 다시 생기니까..?
        self.coupon = self.coupon//10 + self.coupon%10

    
    def check_status(self):
        return self.chicken, self.coupon, self.s_chicken
        
def solution(chicken):
    a = serviceChicken(chicken)
    # self.coupon 이 10장 이내..일 떄 까지 루프 ?
    while a.coupon > 9 : 
        a.get_chicken()
    
    return a.s_chicken