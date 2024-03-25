nums = list(map(int, input().split()))

min_val = mid_val = max_val = nums[0]

for num in nums[1:]:
    if num < min_val:
        max_val, mid_val, min_val = mid_val, min_val, num
        
    elif num > max_val:
        min_val, mid_val, max_val = mid_val, max_val, num
        
    else:
        # 그 외의 경우, 현재 값은 min_val과 max_val 사이
        min_val, mid_val = min_val, num

print(mid_val)
