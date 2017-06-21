

from keras.models import Sequential

from keras.layers.core import Dense

from keras.optimizers import SGD
'''SGD (Stochastic Gradient Descent)'''

from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
'''reshape komutu ile 28x28 piksellik resimlerimizi 784 piksellik birer feature vektörü halinde dönüştürüyoruz:'''
model = Sequential()
model.add(Dense(input_dim=X_train.shape[1],
                output_dim = 50,
                init =   'uniform',
                activation = 'tanh'))
'''Keras’ın Dense layer tipinde. Bu “fully connected layer” olarak da biliniyor. Yani bu katmanın bütün girişleri ve bütün çıkışları birbirine bağlı ve her birinin ayrı bir weighti var. Burada oluşturacağımız ağımız sadece bu tip katmanlardan oluşacak. Bu tip bir ağ mimarisine Multi Layer Perceptron (MLP) deniyor.'''

from keras.layers.core import Activation
from keras.layers.core import Dropout

model.add(Dense(50, init='uniform'))
model.add(Activation('tanh'))
model.add(Dropout(0.5))
model.add(Dense(64, init='uniform'))
model.add(Activation('relu'))

model.add(Dense(10, init='uniform'))
model.add(Activation('softmax'))

from keras.utils.np_utils import to_categorical
y_train_ohe = to_categorical(y_train)


sgd = SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True)

model.compile(loss = 'categorical_crossentropy',
              optimizer = sgd)


model.fit(X_train,
          y_train_ohe,
          nb_epoch = 50,
          batch_size = 500,
          validation_split = 0.1,
          verbose = 1)


y_test_predictions = model.predict_classes(X_test, verbose = 1)


import numpy as np
correct = np.sum(y_test_predictions ==  y_test)
print ('Test Accuracy: ', correct/float(y_test.shape[0])*100.0, '%')


'''from keras.utils.visualize_util import plot
from IPython.display import Image
plot(model, to_file=’model.png’, show_shapes= True)
Image(“model.png”)'''