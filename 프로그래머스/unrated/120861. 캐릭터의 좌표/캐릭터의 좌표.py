def solution(keyinput, board):
    start = [0,0]
    key = {"up": [0,1], "down": [0,-1], "left": [-1,0], "right": [1,0]}
    for k in keyinput:
        if abs(start[0] + key[k][0]) > board[0] // 2 or abs(start[1] + key[k][1]) > board[1] // 2:
            continue
        else:
            start = [start[0] + key[k][0], start[1] + key[k][1]]
            
    return start