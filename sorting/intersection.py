#--------------intersection of two sorted arrays
def intersected(arr1,n1,arr2,n2):
    i=0
    j=0
    while (i<n1 and j<n2):
        if arr1[i]>arr2[j]:
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            print(arr1[i])
            i+=1
            j+=1


print(intersected([1,2,3,4,5],5,[2,3,5,9,10],5))            

