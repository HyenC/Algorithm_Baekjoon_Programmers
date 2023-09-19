N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum_list = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if nums[i] + nums[j] + nums[k] <= M:
                sum_list.append(nums[i] + nums[j] + nums[k])
                
print(sorted(sum_list)[-1])