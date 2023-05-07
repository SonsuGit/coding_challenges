def solution(numbers):
    
    fullnumber=[0,1,2,3,4,5,6,7,8,9]
    
    for i in numbers:
        fullnumber.remove(i)
        
    answer = sum(fullnumber)
    
    return answer