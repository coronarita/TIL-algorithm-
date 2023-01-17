def solution(bin1, bin2):
    # 2진수를 10진수 변환 후 연산해서 재변환
    a = int(bin1, 2)
    b = int(bin2, 2)
    ans = str(bin(a+b))
    return ans[2:]