import sys
input = sys.stdin.readline

N = int(input())
li=[]

for i in range(N):
    li.append(int(input()))

for i in sorted(li):
    print(i)