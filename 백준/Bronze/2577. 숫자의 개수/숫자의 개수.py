result = int(input()) * int(input()) * int(input())
cnt = [0] * 10

for char in str(result):
    cnt[int(char)] += 1

print('\n'.join(map(str, cnt)))