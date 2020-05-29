#-----------  MergeSort  
#divide and conquer algo
#stable algorithm
#theta(nlogn) and O(n) aux space
#in arrays quick sort beats merge sort
#in lists merge sort mainly uses

#------------------------merge two sorted arrays
'''import time
start_time = time.time()


def merge(arr1,n1,arr2,n2):
    i=0
    j=0
    c=[]
    while (i<n1 and j<n2):
        if arr1[i]>arr2[j]:
            c+=[arr2[j]]
            j+=1
        else:
            c+=[arr1[i]]
            i+=1

    while i<n1:
        c+=[arr1[i]]
        i+=1
    while j<n2:
        c+=[arr2[j]]
        j+=1

    return c'''

#print(merge([1,2,3,5,8],5,[2,3,6,7,10],5))  
#print("--- %s seconds ---" % (time.time() - start_time))                     


#-------MERGESORT ALGORITHM

def mergeSMERGE(arr,l,m,r):
    l1=[]
    l2=[]
    c=[]
    i=l
    j=m+1
    while i<m+1:
        l1+=[arr[i]]
    while j<r+1:
        l2+=[arr[j]]
    l=0
    k=0
    while (l<len(l1) and k<len(l2)):
        if l1[l]>l2[k]:
            c+=[l2[k]]
            k+=1
        else:
            c+=[l1[l]]
            l+=1

    while l<len(l1):
        c+=[l1[l]]
        l+=1

    while k<len(l2):
        c+=[l2[k]]
        k+=1
    arr=c
    return arr                   
            




def mergeSort(arr,l,r):
    if r>l:
        m=int(l+((r-l)/2))
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        mergeSMERGE(arr,l,m,r)  

print(mergeSort([3,2,5,6,4,2],0,5))
         















