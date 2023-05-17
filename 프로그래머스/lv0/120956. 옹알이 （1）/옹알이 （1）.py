import re

def solution(babbling):
    word=["aya", "ye", "woo", "ma"]
    result = 0
    
    for i in babbling:
        for j in word:
            i = re.sub(j,' ', i)
        if i.isspace():
            result += 1
            
    return result
    