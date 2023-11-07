def solution(n):
    nums = set()
    d = 2

    while d <= n:
        if n % d == 0:
            nums.add(d)
            n //= d
        else:
            d += 1

    return sorted(list(nums))