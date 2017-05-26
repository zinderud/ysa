# Arsa tahmini basit bir ysa
#import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

num_arsa=120
np.random.seed(40)
arsa_size=np.random.randint(low=200,high=2000,size=num_arsa)#arsa büyüklüğü 200 ile 2000 arası

np.random.seed(40)
arsa_price=arsa_size*100.0+np.random.randint(low=10000,high=100000,size=num_arsa)

#grafik oluşturalım

plt.plot(arsa_size,arsa_price,"bx")
plt.ylabel("price")
plt.xlabel("size")
plt.show();
