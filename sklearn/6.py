
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures



num_arsa=120
np.random.seed(40)
x = np.random.randint(low=200,high=2000,size=num_arsa)
np.random.seed(40)
y = x*100.0+np.random.randint(low=10000,high=100000,size=num_arsa)

x = x.reshape(120, -1)
y = y.reshape(120, -1)

plt.scatter(x,y)
plt.show()

#Lineer Reg.
tahminlineer = LinearRegression()
tahminlineer.fit(x,y)
tahminlineer.predict(x)

plt.plot(x,tahminlineer.predict(x),c="red")

#Polinom Reg.

tahminpolinom = PolynomialFeatures(degree=2)
Xyeni = tahminpolinom.fit_transform(x)

polinommodel = LinearRegression()
polinommodel.fit(Xyeni,y)
polinommodel.predict(Xyeni)

plt.plot(x,polinommodel.predict(Xyeni))

plt.show()

hatakaresilineer = 0
hatakaresipolinom = 0

for i in range(len(Xyeni)):
    hatakaresipolinom = hatakaresipolinom + (float(y[i])-float(polinommodel.predict(Xyeni)[i]))**2

for i in range(len(y)):
    hatakaresilineer = hatakaresilineer + (float(y[i])-float(tahminlineer.predict(x)[i]))**2


 
hatakaresipolinom = 0
    
for a in range(150):

    tahminpolinom = PolynomialFeatures(degree=a+1)
    Xyeni = tahminpolinom.fit_transform(x)

    polinommodel = LinearRegression()
    polinommodel.fit(Xyeni,y)
    polinommodel.predict(Xyeni)
    for i in range(len(Xyeni)):
        hatakaresipolinom = hatakaresipolinom + (float(y[i])-float(polinommodel.predict(Xyeni)[i]))**2
    print(a+1,"inci dereceden fonksiyonda hata,", hatakaresipolinom)

    hatakaresipolinom = 0
 
 

plt.plot(x,polinommodel.predict(Xyeni))

plt.show()

 