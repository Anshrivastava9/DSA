#------------------ QuickSORT implementation from Lomuto Partition

def Lomuto(arr,l,h):
    pivot=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1        



def LQuickSort(arr,l,h):
    if l<h:
        p=Lomuto(arr,l,h)
        LQuickSort(arr,l,p-1)
        LQuickSort(arr,p+1,h)

arr=[1,5,3,10,2,80,40,50,12,3,4,7,89]
#LQuickSort(arr,0,len(arr)-1)
#print(arr)        

def Haore(arr,l,h):
    i=l-1 
    j=h+1
    pivot=arr[l]
    while True:
        i += 1
        while arr[i] < pivot:
            i  += 1
            
           
        j -= 1
        while arr[j] > pivot:
            j -= 1
            
        
        if i>=j:
            return j
        arr[i],arr[j] = arr[j],arr[i]
        
        





def HQuickSort(arr,l,h):
    if l<h:
        p=Haore(arr,l,h)
        HQuickSort(arr,l,p)
        HQuickSort(arr,p+1,h)

HQuickSort(arr,0,len(arr)-1)        
print(arr)



