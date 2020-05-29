#---------simple program to calculate all subsets of given set
def subsets(arr,n,Sum):
    lf=['']
    for i in range(n):
        l=[j+'-'+str(arr[i]) for j in lf]
        lf+=l
  

    b=[]
    for i in range(len(lf)):
        d=lf[i].split('-')
        d=d.pop(0)
        c=[int(z) for z in d]        
        b+=[c]
    print(b)    
    c=0
    for j in range(len(b)):
        if sum(b[j])==Sum:
            c+=1     
    if c==0 and Sum==0:
        print(1)
    else:
        print(c)

subsets([10,5,2,3,6],5,8)    
