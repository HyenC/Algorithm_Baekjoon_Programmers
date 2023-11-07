import re

def solution(new_id):
    # 1단계,2단계
    answer = re.sub('[^0-9a-z_\.-]+','',new_id.lower())
    # 3단계
    answer = re.sub('\.+','.',answer)
    # 4단계
    answer = answer.strip('.')
    # 5단계
    answer = 'a' if answer == '' else answer
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')
    # 7단계
    if len(answer) <= 2:
        answer += answer[-1] * (3-len(answer))
            
    return answer