#here we have to convert string1 to string2 in minimum number of operations
def calc(s1,s2,m,n):
    if m==0:
        return n
    if n==0:
        return m

    if s1[m-1]==s2[n-1]:
        return calc(s1,s2,m-1,n-1)
    else:
        return 1+min(calc(s1,s2,m-1,n),calc(s1,s2,m,n-1),calc(s1,s2,m-1,n-1))

a="amnafkjhjnfjhssjnfshnasjsdnjsdhnsgnrkajokisjg"
b="osajifjsjfrsuiredfsjnfsnshbusbhjsbtygasvghdvestba"
#print(calc(a,b,len(a),len(b)))    

#------Dynamic Programming solution

def solve_Dynamic(s1,s2,m,n):
    dp=[]
    for i in range(n+1):
        a=[]
        for j in range(m+1):
            a+=[0]
        dp+=[a]
            
    for i in range(n+1):
        dp[i][0]=i
    for j in range(m+1):
        dp[0][j]=j
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s2[i-1]==s1[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])


    return dp[n][m]                

print(solve_Dynamic("sunday","saturday",6,8))

