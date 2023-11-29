def solution(polynomial):
    num, xnum = 0, 0
    
    for p in polynomial.split(' + '):
        if p.isdigit():
            num += int(p)
        else:
            xnum = xnum + 1 if p == 'x' else xnum + int(p[:-1])
            
    if xnum == 0:
        return str(num)
    elif xnum == 1:
        return 'x' if num == 0 else f'x + {num}'
    else:
        return f'{xnum}x + {num}' if num != 0 else f'{xnum}x'