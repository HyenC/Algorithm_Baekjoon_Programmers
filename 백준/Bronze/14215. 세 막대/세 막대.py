T = sorted(map(int, input().split()))
if T[2] < T[0] + T[1]:
    print(sum(T))
else:
    print((T[0]+T[1])*2 - 1)