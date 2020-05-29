#-------------- This will group the table according to certain attribute

import pandas as pd

d={'Company':['Fb','Google','Fb','Mrsft','Google'],'SalesPerson':['Vipin','Harsh','Ansh','Deependra','Ansh'],'Rate':[10,15,26,5,25]}


df=pd.DataFrame(d)
#print(df)
#print(df.transpose())

#print(df.groupby('Company'))
#print(df.groupby('Company').min())
#print(df.nlargest(5,['Rate'])) this is out of content
#print(df.groupby('Company').sum())