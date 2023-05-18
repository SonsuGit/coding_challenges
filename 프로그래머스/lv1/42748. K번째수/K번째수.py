def solution(array, commands):
    result = []
    
    for i in commands:
        subarray = array[i[0]-1: i[1]]
        subarray.sort()
        result.append(subarray[i[2]-1])
        
    return result