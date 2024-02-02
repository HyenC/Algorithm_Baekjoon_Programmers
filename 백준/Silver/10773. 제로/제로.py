K = int(input())
s = []

for _ in range(K):
    n = int(input())
    if n == 0:
        s.pop()
    else:
        s.append(n)
        
print(sum(s))