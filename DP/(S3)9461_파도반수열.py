dp = [0]*101

dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

for i in range(6,101):
    dp[i] = dp[i-1] + dp[i-5] # 점화식 p(n) = p(n-1) + p(n-5)

 
T = int(input())
for i in range(T):
    n = int(input())
    print(dp[n])