def check(place):
    people = []
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                people.append((i, j))
                
    for x1, y1 in people:
        for x2, y2 in people:
            dist = abs(x1-x2) + abs(y1-y2)
            if dist == 0 or dist > 2:
                continue
                
            if dist == 1:
                return 0
            elif x1 == x2 and place[x1][int((y1+y2)/2)] != 'X':
                return 0
            elif y1 == y2 and place[int((x1+x2)/2)][y1] != 'X':
                return 0
            elif x1 != x2 and y1 != y2:
                if place[x1][y2] != 'X' or place[x2][y1] != 'X':
                    return 0

    return 1

def solution(places):    
    return [check(place) for place in places]
                
                