def solution(n):
    def hanoi(n, start, end, inter):
        if n == 1:
            return [(start, end)]
        return hanoi(n-1, start, inter, end) + [(start, end)] + hanoi(n-1, inter, end, start)
    
    return hanoi(n, 1, 3, 2)
