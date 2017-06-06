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
num_egitim_ornek=math.floor(num_arsa*0.7)

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

#TensorFlow 
tf_arsa_size=tf.placeholder("float",name="arsa_size")
tf_price=tf.placeholder("float",name="price")

tf_size_factor=tf.Variable(np.random.randn(),name="size_factor")
tf_price_offset=tf.Variable(np.random.randn(),name="price_offset")


 
tf_price_pred=tf.add(tf.multiply(tf_size_factor,tf_arsa_size),tf_price_offset)

#los fonksiyonu tanumlayalım

tf_cost=tf.reduce_sum(tf.pow(tf_price_pred-tf_price,2))/(2*num_egitim_ornek)

#öğrenme hızı
learning_rate = 0.1
#Ogrenme hızını Gradient üzerinde optimize şekilde ilerle
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(tf_cost)


init = tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)

    # set how often to display training progress and number of training iterations
    display_every = 2
    num_training_iter = 50

    # calculate the number of lines to animation
    fit_num_plots = math.floor(num_training_iter/display_every)
    # add storage of factor and offset values from each epoch
    fit_size_factor = np.zeros(fit_num_plots)
    fit_price_offsets = np.zeros(fit_num_plots)
    fit_plot_idx = 0    
    # keep iterating the training data
    for iteration in range(num_training_iter):

        # Fit all training data
        for (x, y) in zip(egitim_arsa_size_norm, egitim_arsa_size_norm):
            sess.run(optimizer, feed_dict={tf_arsa_size: x, tf_price: y})

        # Display current status
        if (iteration + 1) % display_every == 0:
            c = sess.run(tf_cost, feed_dict={tf_arsa_size: egitim_arsa_size_norm, tf_price:eitim_arsa_price_norm})
            print("iteration #:", '%04d' % (iteration + 1), "cost=", "{:.9f}".format(c), \
                "size_factor=", sess.run(tf_size_factor), "price_offset=", sess.run(tf_price_offset))
            # Save the fit size_factor and price_offset to allow animation of learning process
            fit_size_factor[fit_plot_idx] = sess.run(tf_size_factor)
            fit_price_offsets[fit_plot_idx] = sess.run(tf_price_offset)
            fit_plot_idx = fit_plot_idx + 1

    print("Optimization Finished!")
    training_cost = sess.run(tf_cost, feed_dict={tf_arsa_size: egitim_arsa_size_norm, tf_price: eitim_arsa_price_norm})
    print("Trained cost=", training_cost, "size_factor=", sess.run(tf_size_factor), "price_offset=", sess.run(tf_price_offset), '\n')


    # Plot of training and test data, and learned regression
    
    # get values used to normalized data so we can denormalize data back to its original scale
    train_arsa_size_mean = egitim_arsa_size.mean()
    train_arsa_size_std = egitim_arsa_size.std()

    train_price_mean = eitim_arsa_price.mean()
    train_price_std = eitim_arsa_price.std()

    # Plot the graph
    plt.rcParams["figure.figsize"] = (10,8)
    plt.figure()
    plt.ylabel("Price")
    plt.xlabel("Size (sq.ft)")
    plt.plot(egitim_arsa_size, eitim_arsa_price, 'go', label='Training data')
    plt.plot(egitim_arsa_size, eitim_arsa_price, 'mo', label='Testing data')
    plt.plot(egitim_arsa_size_norm * train_arsa_size_std + train_arsa_size_mean,
             (sess.run(tf_size_factor) * egitim_arsa_size_norm + sess.run(tf_price_offset)) * train_price_std + train_price_mean,
             label='Learned Regression')
 
    plt.legend(loc='upper left')
    plt.show()



    # 
    # Plot another graph that animation of how Gradient Descent sequentually adjusted size_factor and price_offset to 
    # find the values that returned the "best" fit line.
    fig, ax = plt.subplots()
    line, = ax.plot(arsa_size, arsa_price)

    plt.rcParams["figure.figsize"] = (10,8)
    plt.title("Gradient Descent Fitting Regression Line")
    plt.ylabel("Price")
    plt.xlabel("Size (sq.ft)")
    plt.plot(egitim_arsa_size, eitim_arsa_price, 'go', label='Training data')
    plt.plot(test_arsa_size, test_arsa_price, 'mo', label='Testing data')

    def animate(i):
        line.set_xdata(egitim_arsa_size_norm * train_arsa_size_std + train_arsa_size_mean)  # update the data
        line.set_ydata((fit_size_factor[i] * egitim_arsa_size_norm + fit_price_offsets[i]) * train_price_std + train_price_mean)  # update the data
        return line,
 
     # Init only required for blitting to give a clean slate.
    def initAnim():
        line.set_ydata(np.zeros(shape=arsa_price.shape[0])) # set y's to 0
        return line,

    ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, fit_plot_idx), init_func=initAnim,
                                 interval=1000, blit=True)

    plt.show()   

