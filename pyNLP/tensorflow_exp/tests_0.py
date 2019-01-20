import unittest

import numpy as np
import tensorflow as tf


class MyTestCase(unittest.TestCase):
    def test_multiply(self):
        a = tf.placeholder("float")
        b = tf.placeholder("float")
        y = tf.multiply(a, b)
        sess = tf.Session()
        actual = sess.run(y, feed_dict={a: 3, b: 3})
        print(actual)


class MyTestCase2(unittest.TestCase):
    def test_lin_reg(self):
        x_data, y_data = self.get_data()
        b, loss, train, w = self.set_variables_for_tf(x_data, y_data)
        self.train_tf(b, loss, train, w)

    def train_tf(self, b, loss, train, w):
        init = tf.initialize_all_variables()
        sess = tf.Session()
        sess.run(init)
        epochs = 8
        for i in range(epochs):
            sess.run(train)
            print("step : {} , w : {}, b : {}, loss : {}".format(i, sess.run(w), sess.run(b), sess.run(loss)))

    def set_variables_for_tf(self, x_data, y_data):
        w = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
        b = tf.Variable(tf.zeros([1]))
        y = w * x_data + b
        loss = tf.reduce_mean(tf.square(y - y_data))
        optimizer = tf.train.GradientDescentOptimizer(0.5)
        train = optimizer.minimize(loss)
        return b, loss, train, w

    def get_data(self):
        num_points = 1000
        vectors_set = []
        for i in range(num_points):
            x1 = np.random.normal(0.0, 0.55)
            y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
            vectors_set.append([x1, y1])
        x_data = [v[0] for v in vectors_set]
        y_data = [v[1] for v in vectors_set]
        return x_data, y_data


if __name__ == '__main__':
    unittest.main()
