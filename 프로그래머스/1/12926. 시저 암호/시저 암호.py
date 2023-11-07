def solution(s, n):
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = A.lower()
    
    answer = ''
    for char in s:
        if char in A:
            i = A.index(char) + n
            answer += A[i%26]
        elif char in a:
            i = a.index(char) + n
            answer += a[i%26]
        else:
            answer += ' '
            
    return answer