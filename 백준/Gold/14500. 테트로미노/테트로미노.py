import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_value = max(map(max, board))
answer = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def tetro(y, x, total, cnt):
    global answer
    if cnt == 4:
        answer = max(answer, total)
        return
    
    elif (total + max_value * (4 - cnt)) <= answer:  # 가지치기
        return

    else:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
        
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = True
                tetro(ny, nx, total + board[ny][nx], cnt + 1)
                visited[ny][nx] = False

# 'ㅜ' 모양 처리를 위한 함수
def check_exc(y, x):
    global answer
    for i in range(4):
        total = board[y][x]
        for j in range(3):
            t = (i+j) % 4
            ny = y + dy[t]
            nx = x + dx[t]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                total = 0
                break
            total += board[ny][nx]
        answer = max(answer, total)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        tetro(i, j, board[i][j], 1)
        visited[i][j] = False
        check_exc(i, j)

print(answer)