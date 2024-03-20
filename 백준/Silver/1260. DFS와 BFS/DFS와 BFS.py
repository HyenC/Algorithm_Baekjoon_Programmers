import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def dfs(V):
    visited[V] = True
    dfs_li.append(V)

    for next_node in sorted(graph[V]):
        if not visited[next_node]:
            dfs(next_node)
            
def bfs(V):
    queue = deque([V])
    visited[V] = True
    
    while queue:
        current_node = queue.popleft()
        bfs_li.append(current_node)
        
        for next_node in sorted(graph[current_node]):
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

N, M, V = map(int, input().split())
graph = defaultdict(list)
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs_li, bfs_li = [], []

dfs(V)
visited = [False] * (N + 1)
bfs(V)

print(*dfs_li)
print(*bfs_li)