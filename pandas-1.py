import pandas as pd
data1={
    'Name':['Jai','Princi','Gaurav','Anuj'],
    'Age':[23,25,26,27],
    'Address':['Mumbai','Delhi','Pune','Chennai'],
    'Qualification':['Msc','Phd','BE','MS']
}

data2={
    'Name':['Ram','Sanya','Girish','Shubham'],
    'Age':[32,26,23,33],
    'Address':['Kolkata','Nagpur','Bangalore','Hyderabad'],
    'Qualification':['Phd','MBA','Bcom','Llb']
}
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
print(df, "\n\n", df1)

frames =[df, df1]
 
res1 =pd.concat(frames)
print("\n\n",res1)