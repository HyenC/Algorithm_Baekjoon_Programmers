def solution(line):
    points = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a*d - b*c != 0:
                x, y = (b*f-e*d) / (a*d-b*c), (e*c-a*f) / (a*d-b*c)
                if int(x) == x and int(y) == y and (x, y) not in points:
                    points.append((int(x), int(y)))
                    
    w_min, w_max = min(points)[0], max(points)[0]
    h_min, h_max = min(points, key = lambda x:x[1])[1], max(points, key = lambda x:x[1])[1]
    
    board = [["."]*(abs(w_max-w_min)+1) for _ in range(abs(h_max-h_min)+1)]
    
    for x, y in points:
        board[h_max-y][x-w_min] = '*'
    
    return [''.join(line) for line in board]