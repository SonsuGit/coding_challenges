from collections import deque

def solution(cacheSize, cities):
    l = [''] * cacheSize
    cache = deque(l, maxlen = cacheSize) # 길이 제한을 하고 
    answer = 0 # 시간

    for city in cities:
        city = city.lower() # 소문자로 다 바꾸고
        if city in cache: # cache hit
            cache.remove(city)
            answer += 1
        else:   # cache miss
            answer += 5
        cache.append(city)

    return answer