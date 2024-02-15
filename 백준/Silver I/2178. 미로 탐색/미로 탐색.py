from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

def bfs():
    visited[0][0] = 1
    queue = deque()
    queue.append((0, 0))
    
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            
            if not (0 <= next_y < N and 0 <= next_x < M):
                continue
                
            if arr[next_y][next_x] == '1' and visited[next_y][next_x] == -1:
                visited[next_y][next_x] = visited[y][x] + 1
                queue.append((next_y, next_x))
bfs()
print(visited[N-1][M-1])
     
