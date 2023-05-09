def solution(n, m):
#     미리 곱해놓음
    mul = n * m
#     나머지값 1로
    r = 1
#     n이 m보다 무조건 크게 고정
    if n < m:
        n,m = m, n
#   나머지가 0이 될때까지 반복
    while(r != 0):
        r = n % m
        n = m
        m = r
    answer = [n, mul/n]
    return answer