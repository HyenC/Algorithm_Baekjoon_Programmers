import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    arr_str = input().strip()[1:-1]
    if arr_str:
        arr = deque(arr_str.split(','))
    else:
        arr = deque()
        
    reverse = False
    error = False
    for i in p:
        if i == 'R':
            reverse = not reverse
        elif i == 'D':
            if arr:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                error = True
                break

    if not error:
        arr = list(arr) if arr else []
        if reverse:
            arr.reverse()
        print(f"[{','.join(arr)}]")