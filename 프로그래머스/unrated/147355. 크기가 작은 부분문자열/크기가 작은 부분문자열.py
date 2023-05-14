def solution(t, p):
    answer = 0
    tl = len(t)
    pl = len(p)
    p = int(p)

    for i in range(tl-pl+1):
        if int(t[i:i+pl]) <= p:
            answer += 1

    return answer

t="3141592"
p='271'

print(solution(t,p))