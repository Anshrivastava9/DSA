#----------------Insertion sort in python
import time
start_time=time.time()
def insertion(arr,n):
    for i in range(n):
        key=arr[i]
        j=i-1
        while (j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

print(insertion([2,1,3,5,4],5))   
print("--- %s seconds ---" % (time.time() - start_time))                     


