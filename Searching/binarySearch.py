#--------------binary search
#1. given sorted array and we have to find the index of element to be searched.

#IP=arr=[1,10,20,40,50,70,80],x=10,
#OP=1
import time
start_time = time.time()

'''def linearSearch(arr,x):
    for i in range(len(arr)):
        if x==arr[i]:
            return i
    return -1     '''

def binarySearch(arr,x,h,l=0):
    mid=int((l+h)/2)
    if l<h:
        return -1
    if x==arr[mid]:
        return mid
    elif x<arr[mid]:
        return binarySearch(arr,x,mid-1,l)
    else:
        return binarySearch(arr,x,h,mid+1)

print(binarySearch([1,2,3,4,5,6,7,8,9,10,12,45,50,78,96,100],0.5,16))



print("--- %s seconds ---" % (time.time() - start_time))            

#----------------------now suppose the given list has repetitions then find the left most index of given element.

#arr=[2,2,3,3,3,3,3,3,3]
#arr=[2,3,3,3,5,5,5,6]

def binarySUpgrade1(arr,x,h,l=0):
    mid=int(l+((h-l)/2))
    if l>h:
        return -1
    if x==arr[mid] and (mid==0 or x!=arr[mid-1]):
        return mid    
    if x<=arr[mid]:
        return binarySUpgrade1(arr,x,mid-1,l)
    else:
        return binarySUpgrade1(arr,x,h,mid+1)  

print(binarySUpgrade1([2,3,3,3,5,5,5,6],3,7))



#---------------------binarySearch in unsorted array
##for peak element question
#--peak element- the element not smaller than neighbours if present.
#corner element can be a peak element
#we have to find only one peak 


def peak(arr,h,l=0):
    mid=int(l+((h-l)/2))
    if mid==0:
        return arr[mid]
    if arr[mid-1]<=arr[mid] and arr[mid]>=arr[mid+1]:
        return arr[mid]
    elif arr[mid]>arr[mid-1]:
        return peak(arr,h,mid+1)
    elif arr[mid]<arr[mid-1] and arr[mid]<arr[mid+1]:
        return peak(arr,mid-1,l)    
    else:
        return peak(arr,mid-1,l)        

#print(peak([10,20,15,5,23,90,67],6))
#print(peak([10,20,3,5,8,7,60],6))

