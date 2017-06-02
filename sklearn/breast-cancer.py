
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

veri = pd.read_csv("data.data")

veri=veri.replace('?', -222, inplace='true')
veri=veri.drop(['id'], axis=1)


y = veri.benormal
x = veri.drop(['benormal'], axis=1)

imp = Imputer(missing_values=-222, strategy="mean",axis=0)
x = imp.fit_transform(x)

 


tahmin = KNeighborsClassifier(n_neighbors=4, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='euclidean', metric_params=None, n_jobs=1)
tahmin.fit(x,y)
ytahmin = tahmin.predict(x)

basari = accuracy_score(y, ytahmin, normalize=True, sample_weight=None)
print("Yüzde",basari*100," oranında:" )

print(tahmin.predict([1,1,1,1,1,1,1,1,1,1]))