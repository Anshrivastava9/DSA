#Two POinter Approach for solving sorted array questions
# @return true if there is a pair present in the array having sum equals to given number
#this is only for sorted array
import time
start_time = time.time()

def Sum(arr,x,h,l=0):#Doubles
    if l==h:
        return False
    if arr[l]+arr[h]==x:
        return True
    elif arr[l]+arr[h]>x:
        return Sum(arr,x,h-1,l)
    else:
        return Sum(arr,x,h,l+1) 


#print(Sum([1,2,3,4,5],0,4))
#print("--- %s seconds ---" % (time.time() - start_time))                     



def Triplet(arr,x,h,l=0):  #triplets
    if l==h:
        return False
    for i in range(l+1,h):
        if arr[l]+arr[h]+arr[i]==x:
            return l+h+i
        elif arr[l]+arr[h]+arr[i]<x:
            return Triplet(arr,x,h,l+1)
        else:
            return Triplet(arr,x,h-1,l) 

'''def TripletNaive(arr,x,h,l=0):
    for i in range(h):
        for j in range(i,h):
            for k in range(j,h):
                if arr[i]+arr[j]+arr[k]==x:
                    return True
    return False

'''
print(Triplet([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],42,14))
#print(TripletNaive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],42,14))
#print("--- %s seconds ---" % (time.time() - start_time))


#------------Pythagoras Question In triplet
# find the triple pair in an arr whose sum is equals to x and follow pythagoras theorem.

def PythagorasTriplet(arr,x,h,l=0):
    if l>=h:
        return False
    for i in range(l+1,h):
        if arr[l]+arr[h]+arr[i]==x and (arr[l]**2==arr[h]**2+arr[i]**2) or (arr[h]**2==arr[l]**2+arr[i]**2) or (arr[i]**2==arr[h]**2+arr[l]**2):
            return True
                  
        elif arr[l]+arr[h]+arr[i]>x:
            return PythagorasTriplet(arr,x,h-1,l)
        else:
            return PythagorasTriplet(arr,x,h,l+1) 
             
     
                               

  
#print(PythagorasTriplet([1,2,3,4,5,6,7,8,9,10],24,9))
#print("--- %s seconds ---" % (time.time() - start_time))


def CountSumPair(arr,x,h,l=0,c=0):
    if l>=h:
        return c
    if arr[l]+arr[h]==x:
        return CountSumPair(arr,x,h-1,l+1,c+1)
    elif arr[l]+arr[h]>x:
        return CountSumPair(arr,x,h-1,l,c)
    else:
        return CountSumPair(arr,x,h,l+1,c) 

#print(CountSumPair([0,1,2,4,5,8,9],9,6))



def CountTriplet(arr,x,h,l=0,c=0):#triplets
    if l>=h:
        return c
    for i in range(l+1,h):
        if arr[l]+arr[h]+arr[i]==x:
            return CountTriplet(arr,x,h-1,l+1,c+1)
        elif arr[l]+arr[h]+arr[i]<x:
            return CountTriplet(arr,x,h,l+1,c)
        else:
            return CountTriplet(arr,x,h-1,l,c)

#print(CountTriplet([1,2,3,4,5,6],9,5))             


