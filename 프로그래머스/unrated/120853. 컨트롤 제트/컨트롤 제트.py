def solution(s):
    s = s.split()
    li = []
    
    for i in s:
        if i == 'Z':
            li.pop()
        else:
            li.append(int(i))
            
    return sum(li)