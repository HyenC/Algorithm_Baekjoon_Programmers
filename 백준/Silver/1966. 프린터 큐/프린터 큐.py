from collections import deque
import sys

T = int(input())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    priorities = list(map(int, sys.stdin.readline().split()))
    
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    cnt = 0
    while queue:
        current = queue.popleft()
        if any(current[0] < other[0] for other in queue):
            queue.append(current)
        else:
            cnt += 1
            if current[1] == M:
                print(cnt)
                break