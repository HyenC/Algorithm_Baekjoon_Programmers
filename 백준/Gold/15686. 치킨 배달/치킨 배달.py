import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
houses = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 1]
chickens = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 2]

def chickens_distance(chosen_chickens):
    total_distance = 0
    for hx, hy in houses:
        distance = min([abs(hx - cx) + abs(hy - cy) for cx, cy in chosen_chickens])
        total_distance += distance
    return total_distance

min_distance = float('inf')
for chosen_chickens in combinations(chickens, M):
    min_distance = min(min_distance, chickens_distance(chosen_chickens))
    
print(min_distance)