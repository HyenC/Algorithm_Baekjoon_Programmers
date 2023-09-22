N = int(input())
s, cnt = [666], 1

while(len(s) < N):
    m = cnt * 1000
    if(cnt % 1000 == 666):
        s += [m + i for i in range(1000)]
    elif(cnt % 100 == 66):
        s += [m + 600 + i for i in range(100)]
    elif(cnt % 10 == 6):
        s += [m + 660 + i for i in range(10)]
    else:
        s += [m + 666]
    cnt += 1

print(s[N - 1])