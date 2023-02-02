def solution(n):
    ans = sorted(str(n), reverse=True)
    return int("".join(ans))