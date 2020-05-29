#--------------theta(n+k) time complexity sorting
#-------k must be linear 

def CountSort(arr,n,k):
    count=[]
    output=[]   # size=k
    for i in range(k):
        count+=[0]
    for i in range(n):
        output+=[0]
    for j in range(n):
        count[arr[j]]+=1

    for i in range(1,k):
        count[i]+=count[i-1]

    for j in range(n-1,-1,-1):
        output[count[arr[j]]-1]=arr[j]
        count[arr[j]]-=1
    print(output)        

CountSort([10,20,3,5,11,12,1],7,21)        
