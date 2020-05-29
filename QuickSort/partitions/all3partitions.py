#------------Naive Partition
#arr=[10,50,30,40,20]

def Naive(arr,n,p):
    l=0
    h=n-1
    temp=[]
    for i in range(n):
        if arr[i]<p:
            temp+=[arr[i]]

    for j in range(n):
        if arr[j]==p:
            temp+=[arr[j]]

    for z in range(n):
        if arr[z]>p:
            temp+=[arr[z]]

    arr=temp
    print(arr)

#Naive([10,5,3,3,4,7,4,9,6],9,4) 
#--------------------Lomuto when pivot is last element
def Lomuto(arr,n):
    p=arr[n-1]
    l=0
    i=l-1
    for j in range(l,n-1):
        if arr[j]<p:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[n-1]=arr[n-1],arr[i+1]
    print(arr)

#Lomuto([10,5,3,3,4,7,4,9,6],9) 

#------------------Hoare Partition when pivot is first element
def Hoare(arr,n):
    p=arr[0]
    l=0
    r=n-1
    while True:
        while True:
            if arr[l]<=p:
                l+=1
            else:
                break

        while True:
            if arr[r]>p:
                r-=1
            else:
                break
        if r>l:        
            arr[r],arr[l]=arr[l],arr[r]
        else:
            print(arr)
            break    


#Hoare([4,5,3,3,7,4,5,4,9,6],10)        




        















