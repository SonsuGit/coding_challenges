def solution(strings, n):
#     문자열을 리스트로 하나하나 나누어서 인덱스별로 분류후 다시 문자열로 합침
    str_list=[]
    ans=[]
    for i in strings:
        str_list.append(list(i))
        
    str_list.sort()
    str_list.sort(key = lambda x :x[n])
    
    
    for i in str_list:
        ans.append("".join(i))
        
    return ans