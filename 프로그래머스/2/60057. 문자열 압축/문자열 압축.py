def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s)//2)+1):
        r = ''
        cnt = 1
        tmp = s[:i]
        
        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    r = r + str(cnt) + tmp
                else:
                    r = r + tmp
                tmp = s[j:i+j]
                cnt = 1
            
        if cnt != 1:
            r = r + str(cnt) + tmp
        else:
            r = r + tmp
        result.append(len(r))
        
    return min(result)