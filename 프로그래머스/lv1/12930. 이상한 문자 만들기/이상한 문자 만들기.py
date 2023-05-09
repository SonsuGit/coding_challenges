def solution(s):
    
    s2l = list(s)
    answer = []
    sindex = 0

    for i in s2l:
        if i == ' ':
            sindex = -1
            answer.append(' ')
        elif sindex % 2 == 0:
            answer.append(i.upper())
            # print(i)
        else:
            answer.append(i.lower())
            # print(i)
        sindex += 1
    answer = ''.join(answer)
    return answer

n = 'tRy this aT hOME'
print(solution(n))