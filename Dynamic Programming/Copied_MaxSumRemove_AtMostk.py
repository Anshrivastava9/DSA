def sol(arr,n,k):
    array_max=[]
    cur_max=0
    for i in range(len(arr)):
        cur_max=max(arr[i]+cur_max,cur_max)
        array_max+=[cur_max]
    print(array_max)
arr=[6,-5,3,-7,6,-1,10,-8,-8,8]
n=len(arr)
k=2
sol(arr,n,k)        