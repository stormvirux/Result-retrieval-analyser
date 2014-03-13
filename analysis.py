import pandas as pd
import numpy
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

#pd.set_option('max_columns', 50)
data=pd.read_csv("output11cs.csv")
#df2 = data.groupby(['Total','Total.1','Total.2','Total.3','Total.4','Total.5','Total.6','Total.7'])['Main Total'].sum().reset_index()
#df2.sum(axis=1)
df3=data[['Total','Total.1','Total.2','Total.3','Total.4','Total.5','Total.6','Total.7']]
print df3
data["Main Total"]=df3.sum(axis=1)
data = data.dropna()
data.reset_index(drop=True)
x=data["Main Total"]
print data["Main Total"]
k_test=stats.kstest(x,"norm")
print sm.stats.lillifors(x)
print k_test
#print df2
#print df2.mean()
"""plt.hist(data["Main Total"])
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()"""
