import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    command = input().split()

    if command[0] == "all":
        S = set(range(1, 21))
        continue
    elif command[0] == "empty":
        S.clear()
        continue

    x = int(command[1])
    
    if command[0] == "add":
        S.add(x)
    elif command[0] == "remove":
        S.discard(x)  # discard 대신 remove를 사용할 경우 요소가 없을 때 에러 발생
    elif command[0] == "check":
        print(1 if x in S else 0)
    elif command[0] == "toggle":
        if x in S:
            S.discard(x)
        else:
            S.add(x)