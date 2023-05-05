def solution(x):
    sum_num = sum([int(i) for i in str(x)])
    if x%sum_num == 0:
        return True
    return False