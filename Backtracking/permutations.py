#Print all permutations of given string which do not have given substring
def isSafe(l,i,string1,r):
    if l!=0 and string1[l-1]=='1' and string1[i]=='2':
        return False
    if r==l+1 and string1[i]=='1' and string1[l]=='2': 
        return False
    return True

def permute(string1,l,r,l1):
    string1=list(string1)
    if l==r:
        string1=''.join(string1)
        l1+=[string1] 
        return    
    else:
        for i in range(l,r+1):                                                                                                                                                                                                                                                                                                                                  
            if isSafe(l,i,string1,r):        
                string1[i],string1[l]=string1[l],string1[i]
                permute(string1,l+1,r,l1) 
                string1[i],string1[l]=string1[l],string1[i]
                
l1=[]
permute("abcdefghij",0,9,l1)
i='fjadchbegi'
if i in l1:
    a=l1.index(i)
    print(l1[a-1])
