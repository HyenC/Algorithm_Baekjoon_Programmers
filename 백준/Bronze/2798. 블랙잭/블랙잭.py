from itertools import combinations
 
N, M = map(int, input().split())
nums = list(map(int, input().split()))
 
result = 0
 
for i in combinations(nums, 3):
    if result < sum(i) and sum(i) <= M:
        result = sum(i)
 
print(result)