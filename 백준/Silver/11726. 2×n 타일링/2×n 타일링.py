t = int(input())
dp = [0 for _ in range(1000)]
dp[0] = 1
dp[1] = 2
for i in range(2,t):
    dp[i] = (dp[i-1]+dp[i-2])
print(dp[t-1]%10007)