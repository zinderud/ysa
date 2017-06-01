"""
            Basic Principles of Machine Learning
After briefly introducing scikit-learn's Estimator object, we'll cover supervised learning, including classification and regression problems, and unsupervised learning, including dimensinoality reduction and clustering problems.

"""
import numpy as np
import matplotlib.pyplot as plt

# use seaborn for plot defaults
# this can be safely commented out
import seaborn; seaborn.set()
from sklearn.linear_model import LinearRegression
model = LinearRegression(normalize=True)
print(model.normalize)
print(model)

x = np.arange(20)
y = 2 * x + 1
plt.plot(x, y, 'o');
plt.show()
X = x[:, np.newaxis]
print(X)
print(y)

# fit the model on our data
model.fit(X, y)



# underscore at the end indicates a fit parameter
print(model.coef_)
print(model.intercept_)

