from collections import defaultdict, deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for node in sorted(graph[start]):
        if node not in visited:
            dfs(graph, node, visited)
    return visited

def bfs(graph, start):
    visited = [start]
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for next_node in sorted(graph[node]):
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)
    return visited

N, M, V = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_result = dfs(graph, V)
bfs_result = bfs(graph, V)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))