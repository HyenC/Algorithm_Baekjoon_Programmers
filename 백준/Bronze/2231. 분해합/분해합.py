N = int(input())

for i in range(max(1, N - len(str(N))*9), N+1):
    if sum(map(int, str(i))) + i == N:
        print(i)
        break
    if i == N:
        print(0)