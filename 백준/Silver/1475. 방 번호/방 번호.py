num = input()
cnt = [0] * 10

for n in num:
    if n == '6' or n == '9':
        cnt[6] += 1
    else:
        cnt[int(n)] += 1
        
cnt[6] = (cnt[6] + 1) // 2
        
print(max(cnt))