import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets


def test_SLNN():
    mnist = read_data_sets("/Users/bhargavayyagari/github/pyNLP/tensorflow_exp/resources/mnist_data/", one_hot=True)
    x = tf.placeholder("float", [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    y_ = tf.placeholder("float", [None, 10])
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

        if i % 100 == 0:
            train_accuracy = sess.run(accuracy, feed_dict={x: batch_xs, y_: batch_ys})
            print("Step %d - Train accuracy %.3f" % (i, train_accuracy))

    test_accuracy = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
    print("Test accuracy %.3f" % test_accuracy)


if __name__ == '__main__':
    test_SLNN()
