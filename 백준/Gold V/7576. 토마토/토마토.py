from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque([(i, j) for i in range(N) for j in range(M) if arr[i][j] == 1])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 0:
                arr[ny][nx] = arr[y][x] + 1
                queue.append((ny, nx))
                
    max_day = 0                
    for row in arr:
        if 0 in row:
            return -1
        max_day = max(max_day, max(row))
        
    return max_day - 1

print(bfs())