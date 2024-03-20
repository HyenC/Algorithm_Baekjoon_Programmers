N = input()

cnt = 0
if len(N) == 1:
    N = '0' + N
new_N = N

while True:
    sum_new_N = str(int(new_N[0]) + int(new_N[1]))
    new_N = new_N[-1] + sum_new_N[-1]
    cnt += 1
    if new_N == N:
        break
    
print(cnt)
