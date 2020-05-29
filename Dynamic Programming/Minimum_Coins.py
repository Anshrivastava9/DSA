def solve_Minimum_Coins(arr,val,temp):
    for i in range(1,val+1):
        for j in range(len(arr)):
            if arr[j]<=i:
                b=i-arr[j]
                temp[i]=min(temp[i],temp[b]+1)

    return temp[val]            




import sys
max1 = sys.maxsize
val=525
temp=[0]
for i in range(1,val+1):
    temp+=[max1]
print(solve_Minimum_Coins([5,20,50,10],val,temp))    