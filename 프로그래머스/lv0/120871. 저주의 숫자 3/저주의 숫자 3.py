def solution(n):
    sum = 0
    for i in range(n):
        sum+=1
        while sum % 3 == 0 or '3' in str(sum):
            sum+=1
    return sum