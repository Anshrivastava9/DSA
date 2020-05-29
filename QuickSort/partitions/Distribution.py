#---------------------Chocolate distribution problem

def Distribute(arr,n,m):
    if n>m:
        arr.sort()    #----complexity(O(nlogn))
        res=arr[m-1]-arr[0]
        for i in range(n-m+1):
            res=min(res,arr[i+m-1]-arr[i])  #--complexity(O(n))
        return res
    else:
        return None

print(Distribute([10,1,4,5,3,7,8,9],8,3))                