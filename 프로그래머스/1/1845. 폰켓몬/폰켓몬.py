import numpy as np

def solution(nums):
    if len(nums) / 2 >= len(np.unique(nums)):
        return len(np.unique(nums))
    else:
        return len(nums) / 2