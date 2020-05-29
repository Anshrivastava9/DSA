 #pandas-- 
'''series
 dataframes
 missing data
 groupby
 merging joining concatening
 operations
 data Input and output'''
 #Series


'''import pandas as pt

data=[1,2,3,4]
labels=['a','b','c','d']
data_dict={'a':1,'b':2,'c':3}

arr1=pt.Series(data)

arr2=pt.Series(data,labels)


arr3=pt.Series(data_dict)

arr4=pt.Series(labels,data)
#print(arr4[1])
#print(arr2['a'])


#print(arr3)

#print(arr2+arr3)


'''
#-------DATA_FRAMES

'''import random 

random.seed(10)
print(random.randint(1,200))
random.seed(11)
print(random.randint(5,200))
random.seed(10)
print(random.randint(200,400))'''
import numpy as np
from numpy.random import randn
np.random.seed(101)
df=pt.DataFrame(randn(5,4),['A','B','C','D','E'],['P','Q','R','S'])

#print(df)

#print(randn(5,4))

ds=pt.DataFrame(randn(4,5),['A','B','C','D'],['P','Q','R','S','T'])
#print(ds)

ds['new']=ds['P']+ds['Q']
#print(ds)

#ds.drop('new') The can only dlt thr row(axis=0)
df=ds.drop('new',axis=1)
#print(df)
#print(ds)#this still has 'new' column 

ds.drop('new',axis=1,inplace=True)
#print(ds)

sp=ds.shape
#print(sp)

da=ds.loc['A']
#print(da)

da1=ds.loc[['A','C'],['P','Q']]
#print(da1)

#----------------------ADVANCE DATAFRAMES

#print(ds)
#conditional statements 
df=ds['P']>0.4
#print(ds[df])

#print(ds[ds['Q']>0.3][['Q','S']])  


#print(ds>0)


print(ds)



#--------------------------------- DATAFRAMES LAST


