import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import datetime
from scipy.stats import linregress

dataset = pd.read_excel("../input/see-level/sea_levels_Predict2025.xlsx")


dataset.head(1000)


dataset.columns

dataset.info()


X = np.arange(1880,1963+(1/12)*4,1/12)
y=dataset.iloc[:,1].values


plt.scatter(X,y,color="red",s=10)
plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.show()


res = linregress(X,y)
print(f"slope {res.slope}")
print(f"intercept {res.intercept}")
print(res)  

X_test = np.arange(1880,2001,1/12)
X_test

y_test = X_test*res.slope
y_test = y_test + res.intercept


plt.scatter(X,y,color="red",s=10)
plt.plot(X_test,y_test,color="green")
plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.show()


for i,item in enumerate(y_test[-12:]):
    print(f'{i+1} : {item}')