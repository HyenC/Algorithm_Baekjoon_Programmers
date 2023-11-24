from collections import defaultdict
from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    summits.sort()
    graph = defaultdict(list)
    
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
        
    hq = []
    visited = [1000000000] * (n + 1)
    for g in gates:
        heappush(hq, (0, g))
        visited[g] = 0
        
    while hq:
        intensity, node = heappop(hq)
        if intensity > visited[node] or node in summits:
            continue
        
        for w, next_node in graph[node]:
            next_intensity = max(intensity, w)
            if next_intensity < visited[next_node]:
                visited[next_node] = next_intensity
                heappush(hq, (next_intensity, next_node))
                
    min_intensity = [0, 1000000000]
    for s in summits:
        if min_intensity[1] > visited[s]:
            min_intensity[0] = s
            min_intensity[1] = visited[s]
    
    return min_intensity