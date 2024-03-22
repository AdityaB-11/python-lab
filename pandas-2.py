import pandas as pd 
data1={
   'key': ['K0', 'K1', 'K2', 'K3'],
   'Name':['Jay','Princi','Gaurav','Anuj'],
   'Age':[27, 24, 22, 32]
}
 
data2={
   'key': ['K0', 'K1', 'K2', 'K3'],
    'Address':['Mumbai','Delhi','Pune','Chennai'],
    'Qualification':['Msc','Phd','BE','MS']
}
df = pd.DataFrame(data1)
 
df1 = pd.DataFrame(data2) 
print(df, "\n\n", df1) 

res =pd.merge(df, df1, on='key')
 
print("\n\n",res)

