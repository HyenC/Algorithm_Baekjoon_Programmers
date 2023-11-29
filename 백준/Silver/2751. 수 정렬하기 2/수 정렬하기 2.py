import sys

N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(N)]

li.sort()
for i in li:
    print(i)