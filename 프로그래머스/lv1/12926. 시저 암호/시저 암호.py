def solution(s, n):
    answer = ''
    s = list(s)
#     chr(int) -> int값에 해당하는 유니코드 문자 반환
#     ord(str) -> str값에 해당하는 유니코드 정수 반환
    for i in s:
        if i.isupper():
            answer += chr((ord(i)-ord('A')+n)%26+ord('A'))
        elif i.islower():
            answer += chr((ord(i)-ord('a')+n)%26+ord('a'))
        else:
            answer += i
    return answer