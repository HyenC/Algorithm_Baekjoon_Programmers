while True:
    tri = sorted(map(int, input().split()))
    
    if tri.count(0) == 3:
        break
    
    if tri[2] < tri[0] + tri[1]:
        if len(set(tri)) == 1:
            print("Equilateral")
        elif len(set(tri)) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")