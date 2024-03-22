import pandas as pd


data1={
    'Name':['Jai','Princi','Gaurav','Anuj'],
    'Age':[23,25,26,27],
    'Address':['Mumbai','Delhi','Pune','Chennai'],
    'Qualification':['Msc','Phd','BE','MS'],
    'Mobile No': [97, 91, 58, 76]
}


data2={
    'Name':['Jai','Princi','Gaurav','Anuj'],
    'Age':[23,25,26,27],
    'Address':['Mumbai','Delhi','Pune','Chennai'],
    'Qualification':['Msc','Phd','BE','MS'],
    'Salary':[1000, 2000, 3000, 4000]
}
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7]) 
 
print(df, "\n\n", df1) 
res2 =pd.concat([df, df1], axis=1, join='inner')
 
print("\n\n",res2)
