def solution(sides):
    max_side, min_side = max(sides), min(sides)
    
    # x가 가장 클 경우
    # max(sides) < x < max(sides) + min(sides)
    case1 = (max_side + min_side) - max_side - 1
    
    # x가 가장 안 클 경우
    # max(sides) < x + min(sides) -> max(sides) - min(sides) < x < max(sides)
    case2 = max_side - (max_side - min_side) - 1
    
    return case1 + case2 + 1    # x가 max(sides)와 같을 때 = 1


# def solution(sides):
#     max_side, min_side = max(sides), min(sides)
#     num = list(range(max_side, sum(sides)))
    
#     for i in range(max_side - min_side + 1, max_side):
#         num.append(i)
    
#     return len(num)
