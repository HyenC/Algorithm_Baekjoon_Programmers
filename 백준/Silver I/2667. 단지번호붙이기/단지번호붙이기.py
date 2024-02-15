import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

def dfs(i, j):
    if not (0 <= i < N and 0 <= j < N) or arr[i][j] == '0' or visited[i][j]:
        return 0
    visited[i][j] = True
    cnt = 1
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        cnt += dfs(ni, nj)
    return cnt

result = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:
            cnt = dfs(i, j)
            result.append(cnt)
            
print(len(result))
for cnt in sorted(result):
    print(cnt)