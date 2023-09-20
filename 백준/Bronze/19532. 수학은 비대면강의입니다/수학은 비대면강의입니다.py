a, b, c, d, e, f = map(int, input().split())

print((e*c-b*f)//(a*e-b*d), (a*f-c*d)//(a*e-b*d))

#for i in range(-999, 1000):
#    for j in range(-999, 1000):
#        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
#            print(i, j)