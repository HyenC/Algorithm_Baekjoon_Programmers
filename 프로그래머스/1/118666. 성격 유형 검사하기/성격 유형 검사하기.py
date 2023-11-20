def solution(survey, choices):
    mbti = ''
    score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for s, c in zip(survey, choices):
        if c < 4:
            score[s[0]] += 4-c
        elif c > 4:
            score[s[1]] += c-4
            
    li = list(score.items())
    
    for i in range(0, 7, 2):
        if li[i][1] < li[i+1][1]:
            mbti += li[i+1][0]
        else:
            mbti += li[i][0]
            
    return mbti