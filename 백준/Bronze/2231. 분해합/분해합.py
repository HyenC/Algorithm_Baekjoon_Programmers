N = int(input())

for i in range(1, N+1):
    if i == N:
        print(0)
    
    each_num = sum(map(int, str(i)))
    total = i + each_num
    if total == N:
        print(i)
        break