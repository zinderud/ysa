
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as plt

num_arsa=120
np.random.seed(40)
x = np.random.randint(low=200,high=2000,size=num_arsa)
np.random.seed(40)
y = x*100.0+np.random.randint(low=10000,high=100000,size=num_arsa)
x = x.reshape(120, -1)
y = y.reshape(120, -1)
ln = lr()  

ln.fit(x,y) # Verilerimizi x ve y eksenine oturttuk.

ln.predict(x) #x'e göre,  tahmin edeceğiz.

m = ln.coef_ # Coefficient - yani katsayı, bu komutla eğimimizi
                          # Yani m i buluyoruz.
b= ln.intercept_ # Intercept - b dir. yani y = mx+b 'de x'e sıfır 
                              # verdiğimizde kalan değer.

a = np.arange(2500)

plt.scatter(x,y) # Gerçek verilerimizi nokta nokta, scatter ile cizdiriyoruz.
plt.scatter(a,m*a+b, c="red",marker=">")
plt.show()
 

print('Eğim: ', ln.coef_)
print('Y de kesiştiği yer: ', ln.intercept_)


print("Denklem")
print("y=",m,"x+",b)



