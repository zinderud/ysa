import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures as pf
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron
from sklearn import linear_model


num_arsa=120
np.random.seed(40)
x = np.random.randint(low=200,high=2000,size=num_arsa)
np.random.seed(40)
y = x*100.0+np.random.randint(low=10000,high=100000,size=num_arsa)


x = np.array(x)
y= np.array(y)

a,b =  np.polyfit(x,y,1)


z = np.arange(150)

plt.scatter(x,y)

plt.plot(z,a*(z**1)+b*(z**2))
plt.show()