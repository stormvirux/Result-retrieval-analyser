import pandas as pd
import numpy
import matplotlib.pyplot
pd.set_option('max_columns', 50)
data=pd.read_csv("output11cs.csv")
#df2 = data.groupby(['Total','Total.1','Total.2','Total.3','Total.4','Total.5','Total.6','Total.7'])['Main Total'].sum().reset_index()
#df2.sum(axis=1)
df3=data[['Total','Total.1','Total.2','Total.3','Total.4','Total.5','Total.6','Total.7']]
data["Main Total"]=df3.sum(axis=1)
data = data.dropna()
data.reset_index(drop=True)
print data["Main Total"]
#print df2
#print df2.mean()

