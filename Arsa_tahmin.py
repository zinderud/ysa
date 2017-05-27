# 
#  Arsa_tahmin.py
#
#  ysa uygulama örneği
#  Arsa tahmini basit bir ysa

import tensorflow as tf
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

#verileri normalize edecek fonk
def normalize(array):
    return(array-array.mean())/array.std()

# eğitim dataları %70 alalım
num_egitim_ornek=math.floor(num_arsa*0.7z)

# egitim dataları tanımlayalım
egitim_arsa_size=np.asarray(arsa_size[:num_egitim_ornek])
eitim_arsa_price=np.asanyarray(arsa_price[:num_egitim_ornek:])

#normalize edelim
egitim_arsa_size_norm=normalize(egitim_arsa_size)
eitim_arsa_price_norm=normalize(eitim_arsa_price)

#test dataları tanımlayalım
test_arsa_size=np.array(arsa_size[num_egitim_ornek:])
test_arsa_price=np.array(arsa_price[num_egitim_ornek:])

#normalize edelim
test_arsa_size_norm=normalize(test_arsa_size)
test_arsa_price_norm=normalize(test_arsa_price)



