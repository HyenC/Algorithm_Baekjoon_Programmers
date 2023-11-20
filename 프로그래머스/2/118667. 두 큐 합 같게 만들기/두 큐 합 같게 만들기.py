from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    total = s1 + s2
    cnt, limit = 0, len(q1) * 3
    
    if total % 2 != 0:
        return -1
    
    while True:
        if s1 > s2:
            a = q1.popleft()
            q2.append(a)
            s1 -= a
            s2 += a
            cnt += 1
        elif s1 < s2:
            a = q2.popleft()
            q1.append(a)
            s2 -= a
            s1 += a
            cnt += 1
        else:
            break
            
        if cnt == limit:
            return -1
    return cnt