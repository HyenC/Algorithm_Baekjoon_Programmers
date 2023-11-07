def solution(arr1, arr2):
    board = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            
            for k in range(len(arr1[i])):
                board[i][j] += arr1[i][k] * arr2[k][j]
                
    return board