import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
from numpy.random import randn
import matplotlib as mpl
import seaborn as sns

sns.set_color_palette("deep", desat=.6)
mpl.rc("figure", figsize=(8, 4))

#pd.set_option('max_columns', 50)
data=pd.read_csv("output11cs.csv")
df3=data[['Total','Total.1','Total.2','Total.3','Total.4','Total.5','Total.6','Total.7']]
data["Main Total"]=df3.sum(axis=1)
data = data.dropna()
data.reset_index(drop=True)
x=data["Main Total"]
y = stats.uniform.rvs(size = 100)
print stats.kstest(x,'norm')
print stats.normaltest(x)
print sm.stats.lillifors(x)
#plt.hist(x, 70, histtype="stepfilled", alpha=.7);
#max_data = np.r_[data["Main Total"]].max()
#bins = np.linspace(0, max_data, max_data + 1)
plt.hist(data["Main Total"],alpha=.7,linewidth=0)
#plt.hist(data["Total.1"],20,normed=True, color="#6495ED", alpha=.7)
#plt.hist(data['Total.2'],20, normed=True, color="#F08080", alpha=.7)
#plt.hist(data['Total.3'],20, normed=True, color="#8C1515", alpha=.7)
#plt.hist(data['Total.4'],20, normed=True, color="#D2C295", alpha=.7)
#plt.hist(data['Total.5'],20, normed=True, color="#4168B7", alpha=.7)
#sns.lmplot("Total.1", "Total", data)
#sns.kdeplot(data['Main Total'], shade=True)
plt.title("Total marks Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
"""freq=data["Main Total"].value_counts()
dick=dict(freq)
t_data = pd.DataFrame([[key,dick[key]] for key in dick], columns=['lol','rofl'])
plt.axis([200, 800, 0, 2])
plt.plot(t_data["lol"],t_data["rofl"],'bs' )
plt.show()"""


