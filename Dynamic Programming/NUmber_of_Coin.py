def getCount(coins,n,sum):
    if sum==0:
        return 1
    if n==0:
        return 0
    res=getCount(coins,n-1,sum)
    if coins[n-1]<=sum:
        res=res+getCount(coins,n,sum-coins[n-1]) 

    return res

print(getCount([1,2,3],3,4))    

