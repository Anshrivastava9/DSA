def solve(n):
    dp=[1,1,2]
    res=0
    for i in range(3,n+1):
        a=0
        for j in range(i):
            a+=dp[j]*dp[i-j-1]
        dp+=[a]

    print(dp[n])     

solve(250)