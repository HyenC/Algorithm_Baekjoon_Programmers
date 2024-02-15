import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

dy = (-1, -1, -1, 1, 1, 1, 0, 0)
dx = (-1, 0, 1, -1, 0, 1, -1, 1)

def dfs(y, x):
    visited[y][x] = True
    for i in range(8):
        next_y = y + dy[i]
        next_x = x + dx[i]
        if (0 <= next_y < h) and (0 <= next_x < w):
            if not visited[next_y][next_x] and arr[next_y][next_x]:
                dfs(next_y, next_x)
    
while True:
    w, h = map(int, input().split())
    if not (w and h):
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    
    cnt = 0
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)