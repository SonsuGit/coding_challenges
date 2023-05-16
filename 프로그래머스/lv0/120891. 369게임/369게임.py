import re

def solution(order):
    p = re.compile('[369]')
    result = p.findall(str(order))
    return len(result)