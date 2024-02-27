import sys
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))
M = int(input())
board = list(map(int, input().split()))

for num in board:
    print(1 if num in cards else 0, end=' ')