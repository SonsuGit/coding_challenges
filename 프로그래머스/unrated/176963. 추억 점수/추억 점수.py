def solution(name, yearning, photo):
    result = []
    namedict = dict(zip(name, yearning))
    for i in photo:
        sum = 0
        for j in i:
            sum += namedict.get(j, 0)
        result.append(sum)

    return result