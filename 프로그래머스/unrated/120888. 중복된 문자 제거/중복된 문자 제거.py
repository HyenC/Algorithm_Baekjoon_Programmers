def solution(my_string):
    li = []
    for i in list(my_string):
        if i not in li:
            li.append(i)
            
    return ''.join(li)