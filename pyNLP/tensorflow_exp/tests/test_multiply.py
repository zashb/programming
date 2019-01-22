import tensorflow as tf


def test_multiply():
    a = tf.placeholder("float")
    b = tf.placeholder("float")
    y = tf.multiply(a, b)
    sess = tf.Session()
    actual = sess.run(y, feed_dict={a: 3, b: 3})
    print(actual)


if __name__ == '__main__':
    test_multiply()
