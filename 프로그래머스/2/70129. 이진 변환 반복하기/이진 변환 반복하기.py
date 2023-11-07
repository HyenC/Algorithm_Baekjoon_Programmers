def solution(s):
    cnt = 0
    z_cnt = 0
    while s != '1':
        z_cnt += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        cnt += 1
        
    return [cnt,z_cnt]