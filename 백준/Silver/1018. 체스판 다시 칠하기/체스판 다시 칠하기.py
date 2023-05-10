n, m = map(int, input().split())
board =[]
result=[]
for _ in range(n):
    board.append(list(map(str,input())))

# 8*8짜리 보드로 다 테스트하기 위해 나눔
for i in range(0, n-7):
    for j in range(0, m-7):
        # 왼쪽 위가 b일때
        cnt_b = 0
        # 왼쪽 위가 w일때
        cnt_w = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                # 인덱스 합이 짝수인 경우 B
                if (x+y) % 2 == 0:
                    # 0,0 값이 B인 경우
                    if board[x][y] != 'W':
                        cnt_b += 1
                    # 0,0 값이 W인 경우
                    if board[x][y] != 'B':
                        cnt_w += 1
                # 인덱스 합이 홀수인 W
                else:
                    # 0,0 값이 W인 경우
                    if board[x][y] != 'W':
                        cnt_w += 1
                    # 0,0 값이 B인 경우
                    if board[x][y] != 'B':
                        cnt_b += 1
        result.append(cnt_b)
        result.append(cnt_w)
 
print(min(result))
