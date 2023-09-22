import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temps = list(map(int, input().split()))
sums = []
sums.append(sum(temps[:k]))

for i in range(n-k):
    sums.append(sums[i] - temps[i] + temps[i+k])

print(max(sums))