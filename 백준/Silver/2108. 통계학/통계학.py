import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

print(round(sum(arr) / len(arr)))    # 산술평균
print(arr[len(arr) // 2])    # 중앙값

dic = {}    # 최빈값
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
mx = max(dic.values())
freq = [i for i in dic if mx == dic[i]]
        
if len(freq) > 1:
    print(freq[1])
else:
    print(freq[0])
    
print(arr[-1] - arr[0])    # 범위