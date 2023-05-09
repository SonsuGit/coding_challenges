def solution(arr1, arr2):
    answer = []
#     zip으로 arr1, arr2의 2차원을 1차원으로 벗겨냄
    for i,j in zip(arr1, arr2) :
#         두번째 zip으로 원소들 (ex [1,2]와 [3,4])를 묶음
#         리스트 컴프리헨션
        answer.append([x+y for x,y in zip(i,j)])
        
    return answer