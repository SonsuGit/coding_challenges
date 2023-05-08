def solution(left, right):
    answer = 0
#     약수 구하는 함수
    def div(x):
        sum = 0
#         약수 갯수 구하기
        for i in range(1,x//2+1):
            if x % i == 0:
                sum+=1
        sum+=1
#         약수의 갯수가 짝수면
        if sum % 2 == 0:
            return True
        else:
            return False
        
    for i in range(left,right+1):
        if div(i):
            answer+=i
        else:
            answer-=i
            
    return answer