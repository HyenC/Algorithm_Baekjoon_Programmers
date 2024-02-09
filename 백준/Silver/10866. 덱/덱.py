import sys
input = sys.stdin.readline

N = int(input())
deque = []

for _ in range(N):
    com = input().split()
    
    if com[0] == 'push_front':
        deque.insert(0, com[1])
    elif com[0] == 'push_back':
        deque.append(com[1])
    elif com[0] == 'pop_front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
            deque.pop(0)
    elif com[0] == 'pop_back':
        if not deque:
            print(-1)
        else:
            print(deque[-1])
            deque.pop()
    elif com[0] == 'size':
        print(len(deque))
    elif com[0] == 'empty':
        if not deque:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
    else:
        if not deque:
            print(-1)
        else:
            print(deque[-1])