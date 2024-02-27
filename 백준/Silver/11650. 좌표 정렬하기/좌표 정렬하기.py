import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
points.sort(key=lambda x: (x[0], x[1]))

output = '\n'.join(f'{x} {y}' for x, y in points)
print(output)