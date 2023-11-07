def solution(numbers, k):
    if k == 1:
        return numbers[0]
    
    else:
        return numbers[2 * (k-1) % len(numbers)]