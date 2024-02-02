Num = set(range(1, 10001))
NonSelfNum = set()

for i in Num:
    for j in str(i):
        i += int(j)
    NonSelfNum.add(i)
    
SelfNum = sorted(Num - NonSelfNum)
for n in SelfNum:
    print(n)