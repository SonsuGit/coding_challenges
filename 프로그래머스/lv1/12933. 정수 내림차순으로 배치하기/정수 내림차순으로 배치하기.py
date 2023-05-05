def solution(n):
    x = list(str(int(n)))
    x.sort()
    x.reverse()
    return int(("".join(x)))