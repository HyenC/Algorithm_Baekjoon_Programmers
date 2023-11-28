def solution(numbers):
    sorted_numbers = sorted(numbers)
    
    max_num = sorted_numbers[-1]
    second_max = sorted_numbers[-2]
    
    min_num = sorted_numbers[0]
    second_min = sorted_numbers[1]
    
    return max_num * second_max if max_num * second_max > min_num * second_min else min_num * second_min