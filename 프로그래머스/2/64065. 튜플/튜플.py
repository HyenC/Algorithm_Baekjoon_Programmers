def solution(s):
    answer = []
    s = sorted(s[2:-2].split('},{'), key = len)
    for i in s:
        li = i.split(',')
        for j in li:
            if int(j) not in answer:
                answer.append(int(j))
    return answer