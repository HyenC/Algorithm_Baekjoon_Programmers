N, M = map(int, input().split())
board = []
cnt = []

for _ in range(N):
    board.append(input())
    
for i in range(N-7):
    for j in range(M-7):
        start_w = 0
        start_b = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        start_w += 1
                    else:
                        start_b += 1
                else:
                    if board[a][b] != 'W':
                        start_b += 1
                    else:
                        start_w += 1
                        
        cnt.append(start_w)
        cnt.append(start_b)
print(min(cnt))