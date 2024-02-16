from collections import deque
from itertools import combinations
from copy import deepcopy
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
empty_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
virus_positions = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(lab_copy):
    queue = deque(virus_positions)
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and lab_copy[ny][nx] == 0:
                lab_copy[ny][nx] = 2
                queue.append((ny, nx))
    return sum(row.count(0) for row in lab_copy)

max_safe_area = 0
for walls in combinations(empty_spaces, 3):
    lab_copy = deepcopy(lab)
    for y, x in walls:
        lab_copy[y][x] = 1
    safe_area = bfs(lab_copy)
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)