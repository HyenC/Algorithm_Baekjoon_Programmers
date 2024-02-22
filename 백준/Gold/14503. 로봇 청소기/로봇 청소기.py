import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def clean(r, c, d):
    cnt = 0
    
    while True:
        if visited[r][c] == 0:
            visited[r][c] = 1
            cnt += 1
            
        found = False
        for _ in range(4):
            d = (d - 1) % 4
            ny, nx = r + dy[d], c + dx[d]

            if 0 <= ny < N and 0 <= nx < M and room[ny][nx] == 0 and visited[ny][nx] == 0:
                r, c = ny, nx
                found = True
                break
                
        if not found:
            ny, nx = r - dy[d], c - dx[d]
            if 0 <= ny < N and 0 <= nx < M and room[ny][nx] == 0:
                r, c = ny, nx
            else:
                return cnt
            
print(clean(r, c, d))