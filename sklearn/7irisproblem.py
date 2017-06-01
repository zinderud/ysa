"""
Quick Question:

If we want to design an algorithm to recognize iris species, what might the data be?

Remember: we need a 2D array of size [n_samples x n_features].

    What would the n_samples refer to?

    What might the n_features refer to?

Remember that there must be a fixed number of features for each sample, and feature number i must be a similar kind of quantity for each sample.
Loading the Iris Data with Scikit-Learn

Scikit-learn has a very straightforward set of data on these iris species. The data consist of the following:

    Features in the Iris dataset:
        sepal length in cm
        sepal width in cm
        petal length in cm
        petal width in cm

    Target classes to predict:
        Iris Setosa
        Iris Versicolour
        Iris Virginica

scikit-learn embeds a copy of the iris CSV file along with a helper function to load it into numpy arrays:

"""

from sklearn.datasets import load_iris
iris = load_iris()
print(iris.keys())

n_samples, n_features = iris.data.shape
print((n_samples, n_features))
print(iris.data[0])
print(iris.data.shape)
print(iris.target.shape)
print(iris.target_names)

import numpy as np
import matplotlib.pyplot as plt

x_index = 0
y_index = 1

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.scatter(iris.data[:, x_index], iris.data[:, y_index],
            c=iris.target, cmap=plt.cm.get_cmap('RdYlBu', 3))
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.clim(-0.5, 2.5)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index]);
plt.show()