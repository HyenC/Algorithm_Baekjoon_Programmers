import sys
input = sys.stdin.readline

N = int(input())
points = list(map(int, input().split()))
sorted_points = sorted(set(points))

index_dict = {point: index for index, point in enumerate(sorted_points)}

result = ' '.join(str(index_dict[p]) for p in points)
print(result)
