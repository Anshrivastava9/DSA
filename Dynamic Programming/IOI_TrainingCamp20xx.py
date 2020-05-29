def solve1(ar,k,max1,n):
    if n==1:
        max1=max(ar[0],max1)
        return max1

    arr1=sorted(ar)
    for i in range(len(arr1)):
        if i<k:
            if ar[0]<0:
                ar[0].pop(0)
        else:
            break

    max1=max(max1,sum(arr1))
    arr2=ar
    return max(max1,solve1(ar.pop(0),k,max1,n-1),solve1(arr2.pop(-1),k,max1,n-1))
    
arr=[3,4,-1,-5,4]
k=1
max1=0
n=len(arr)

print(solve1(arr,k,max1,n))



