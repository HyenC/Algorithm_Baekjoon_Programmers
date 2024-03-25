A = int(input())
B = int(input())
C = int(input())

nums = [0] * 10
mul_nums = str(A * B * C)

for num in mul_nums:
    if num == '0':
        nums[0] += 1
    elif num == '1':
        nums[1] += 1
    elif num == '2':
        nums[2] += 1
    elif num == '3':
        nums[3] += 1
    elif num == '4':
        nums[4] += 1
    elif num == '5':
        nums[5] += 1
    elif num == '6':
        nums[6] += 1
    elif num == '7':
        nums[7] += 1
    elif num == '8':
        nums[8] += 1
    else:
        nums[9] += 1
        
print('\n'.join(map(str, nums)))