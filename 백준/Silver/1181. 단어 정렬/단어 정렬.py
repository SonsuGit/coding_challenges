n = int(input())
result = []

for i in range(n):
    result.append(input())

setresult = set(result)
result = list(setresult)
result.sort()
result.sort(key= len)

for i in result:
    print(i)