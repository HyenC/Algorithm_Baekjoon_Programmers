def solution(phone_number):
    answer = ''
    b_num = phone_number[-4:]
    f_num= (len(phone_number) - 4) * '*'
    
    return f_num + b_num