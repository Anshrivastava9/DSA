#-------------We have to segregate an array according to given condition
#--I/O=arr=[10,13,14,7] we have to segregate even ones on the left half and odd ones on the right half(order doesn't matter)
# #----O/P=arr=[14,10,7,13] 

def Segregate(arr,n):
    i=-1
    j=n
    while True:
        i+=1
        while arr[i]%2==0:
            i+=1
        j-=1    
        while arr[j]%2!=0:
            j-=1
        if i>=j:
            return
        arr[i],arr[j]=arr[j],arr[i]

arr=[10,13,7,14]
Segregate(arr,4)
#print(arr)


