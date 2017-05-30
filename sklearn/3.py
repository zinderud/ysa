import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
 
num_arsa=120
np.random.seed(40)
x = np.random.randint(low=200,high=2000,size=num_arsa)
np.random.seed(40)
y = x*100.0+np.random.randint(low=10000,high=100000,size=num_arsa)
 

print(x)
print(y)  

plt.scatter(x,y)  
 

m,b = np.polyfit(x,y,1) # np.polyfit(x ekseni, y ekseni, kaçıncı dereceden polinom denklemi) 


a = np.arange(2299)  

plt.scatter(x,y) # Scatter ile nokta çizdirimi yapıyoruz.
plt.plot(m*a+b) # 


z = 32
tahmin = m*z+b
print(tahmin)

plt.scatter(z,tahmin,c="red",marker=">")

plt.show()
print("y=",m,"x+",b)