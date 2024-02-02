def d(n):
    return n + sum(map(int, str(n)))

NonSelfNum = set()
for i in range(1, 10001):
    di = d(i)
    if di <= 10000:  # 10000을 넘지 않는 생성자에 대해서만 처리
        NonSelfNum.add(di)

SelfNum = sorted(set(range(1, 10001)) - NonSelfNum)
print('\n'.join(map(str, SelfNum)))