tri = []

for _ in range(3):
    a = int(input())
    tri.append(a)

if sum(tri) == 180:
    if len(set(tri)) == 1:
        print("Equilateral")
    elif len(set(tri)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")