import sys

K = int(sys.stdin.readline().strip())
s = []
total_sum = 0

for _ in range(K):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        total_sum -= s.pop()
    else:
        s.append(n)
        total_sum += n
        
print(total_sum)  # 리스트를 다시 순회할 필요 없이 결과 출력