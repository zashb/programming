import matplotlib
import numpy as np
import tensorflow as tf

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def test_clustering():
    num_clusters = 3
    num_steps = 100
    vector_values = get_data()
    plot_data(vector_values)
    assignment_values = cluster_data(num_clusters, num_steps, vector_values)
    plot_clusters(assignment_values, vector_values)


def plot_clusters(assignment_values, vector_values):
    data = {"x": [], "y": [], "cluster": []}
    for i in range(len(assignment_values)):
        data["x"].append(vector_values[i][0])
        data["y"].append(vector_values[i][1])
        data["cluster"].append(assignment_values[i])
    df = pd.DataFrame(data)
    sns.lmplot("x", "y", data=df,
               fit_reg=False, size=7,
               hue="cluster", legend=False)
    plt.show()


def cluster_data(num_clusters, num_steps, vector_values):
    vectors = tf.constant(vector_values)
    tf_slice = tf.slice(tf.random_shuffle(vectors), [0, 0], [num_clusters, -1])
    centroids = tf.Variable(tf_slice)
    expanded_vectors = tf.expand_dims(vectors, 0)
    expanded_centroids = tf.expand_dims(centroids, 1)
    print(expanded_vectors.get_shape())
    print(expanded_centroids.get_shape())
    subtract = tf.subtract(expanded_vectors, expanded_centroids)
    distances = tf.reduce_sum(tf.square(subtract), 2)
    assignments = tf.argmin(distances, 0)
    means = tf.concat(axis=0, values=[
        tf.reduce_mean(
            tf.gather(vectors,
                      tf.reshape(
                          tf.where(
                              tf.equal(assignments, c)
                          ), [1, -1])
                      ), axis=[1])
        for c in range(num_clusters)])
    update_centroids = tf.assign(centroids, means)
    init_op = tf.global_variables_initializer()
    # with tf.Session('local') as sess:
    sess = tf.Session()
    sess.run(init_op)
    for step in range(num_steps):
        _, centroid_values, assignment_values = sess.run([update_centroids,
                                                          centroids,
                                                          assignments])
    print("centroids")
    print(centroid_values)
    return assignment_values


def plot_data(vector_values):
    df = pd.DataFrame({"x": [v[0] for v in vector_values],
                       "y": [v[1] for v in vector_values]})
    sns.lmplot("x", "y", data=df, fit_reg=False, size=7)
    plt.show()


def get_data():
    num_vectors = 1000
    vector_values = []
    for i in range(num_vectors):
        if np.random.random() > 0.5:
            vector_values.append([np.random.normal(0.5, 0.6),
                                  np.random.normal(0.3, 0.9)])
        else:
            vector_values.append([np.random.normal(2.5, 0.4),
                                  np.random.normal(0.8, 0.5)])
    return vector_values


if __name__ == '__main__':
    test_clustering()
