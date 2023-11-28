def solution(numbers):
    numbers = sorted(numbers)
    
    max_num = numbers[-1]
    second_max = numbers[-2]
    
    min_num = numbers[0]
    second_min = numbers[1]
    
    return max(max_num * second_max, min_num * second_min)