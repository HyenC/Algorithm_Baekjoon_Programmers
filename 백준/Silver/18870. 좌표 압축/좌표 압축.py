import sys
input = sys.stdin.readline

N = int(input())
points = list(map(int, input().split()))
sorted_points = sorted(set(points))

dict = {point: index for index, point in enumerate(sorted_points)}

for p in points:
    print(dict[p], end=' ')
