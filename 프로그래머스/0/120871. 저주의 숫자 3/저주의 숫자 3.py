def solution(n):
    non_three = 1
    cnt = 0
    
    while cnt < n:
        if non_three % 3 != 0 and '3' not in str(non_three):
            cnt += 1
        non_three += 1
    
    return non_three - 1