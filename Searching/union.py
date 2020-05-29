#------------------------ Union of two sorted arrays

def union(arr1,n1,arr2,n2):
    i=0
    j=0
    while (i<n1 and j<n2):
        while i<n1-1 and arr1[i]==arr1[i+1]:
            i+=1
        while j<n2-1 and arr2[j]==arr2[j+1]:
            j+=1
        
        if arr1[i]>arr2[j]:
            print(arr2[j],end=" ")
            j+=1
                  
        elif arr1[i]<arr2[j]:
            print(arr1[i],end=" ")
            i+=1
        else:
            print(arr1[i],end=" ")
            i+=1
            j+=1

    while i<n1:
        print(arr1[i],end=" ")
        i+=1
    while j<n2:
        print(arr2[j],end=" ")
        j+=1


union([1,2,3,4,4,4,5],7,[3,4,5,5,6,7],6)                        
