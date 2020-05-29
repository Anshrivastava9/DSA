#-------------------Three Way Partitioning Algorithm.
#Suppose we have to partition 0's,1's,2's in only on iteration.

def ThreeWayPartition(arr,n):
    l=0
    m=0
    h=n-1
    while True:
        if arr[m]==0:
            arr[l],arr[m]=arr[m],arr[l]
            l+=1
            m+=1
        elif arr[m]==1:
            m+=1        
        else:
            arr[h],arr[m]=arr[m],arr[h]
            h-=1 

        if m>=h:
            return arr

#print(ThreeWayPartition([0,1,2,0,1,1,2],7))   


#--------------Now Divide the range of numbers in a List
#suppose partition the array in a range(5,11) and left most elements are less than range and right most elements are greater than that
#arr=[6,1,7,2,3,9,12,18,3,19] ==arr=[2,1,3,3,6,7,18,12,19]

def ThreeWayPartitionRange(arr,n):
    l=0
    m=0
    h=n-1
    while True:
        if arr[m]<27:
            arr[m],arr[l]=arr[l],arr[m]
            l+=1
            m+=1
        elif arr[m]>=27 and arr[m]<=40:
            m+=1
        else:
            arr[m],arr[h]=arr[h],arr[m]
            h-=1

        if m>h:
            return arr

print(ThreeWayPartitionRange([7, 96, 40, 50, 21, 68],6))                       



