def solution(sizes):
#     sizes 리스트를 받아서 가로, 세로길이를 바꾸면 
#     2*2*2*2의 16개가 생성됨
#     16개마다 지갑크기를 반환해서 리스트에 저장
#     지갑크기리스트의 min값 반환하면 끝
#     라고 생각했으니 사이즈의 길이가 너무 길면 너무 오래걸려 안됨

    big = []
    small = []

    for i in sizes:
        if i[0]>i[1]:
            big.append(i[0])
            small.append(i[1])
        else:
            big.append(i[1])
            small.append(i[0])

    return max(big)*max(small)
        