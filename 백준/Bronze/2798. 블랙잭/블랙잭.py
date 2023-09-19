N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)

result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            current_sum = nums[i] + nums[j] + nums[k]
            if result < current_sum and current_sum <= M:
                result = current_sum
                break    
print(result)