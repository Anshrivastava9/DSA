#--------------Recursive Solution
#=====O(3Pn) solution
import sys
sys.setrecursionlimit(1500)
def solve_recursive(n,a,b,c):
    if n==0:
        return 0
    if n<0:
        return -1

    res=max(solve_recursive(n-a,a,b,c),solve_recursive(n-b,a,b,c),solve_recursive(n-c,a,b,c))

    if res==-1:
        return res
    else:
        return res+1



#print(solve_recursive(800,1,200,500))

def maxCuts_DynamicSol(n,a,b,c):
    dp=[]
    dp+=[0]
    for i in range(1,n+1):
        dp+=[-1]
        if i-a>=0:
            dp[i]=max(dp[i],dp[i-a])
        if i-b>=0:
            dp[i]=max(dp[i],dp[i-b])
        if i-c>=0:
            dp[i]=max(dp[i],dp[i-c])
        
        if dp[i]!=-1:
            dp[i]+=1
    return dp[n]


print(maxCuts_DynamicSol(23,11,12,13))    












