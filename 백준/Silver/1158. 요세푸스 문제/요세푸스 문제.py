N, K = map(int,input().split())
index = 0
li = list(range(1, N+1))
result = []

while li:
    index += (K-1)
    index = index % len(li)
    result.append(str(li.pop(index)))

print("<" + ", ".join(result) + ">")