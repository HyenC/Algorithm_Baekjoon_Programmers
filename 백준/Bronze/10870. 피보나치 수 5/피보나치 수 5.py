n = int(input())

def fibo(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    if n > 0:    # n이 0일 수도 있기 때문에
        dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

print(fibo(n))
