from sklearn.manifold import TSNE
# from sklearn.datasets import load_iris, fetch_20newsgroups,
from sklearn.datasets import load_iris, load_digits
from sklearn.decomposition import PCA

from matplotlib import offsetbox
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from time import time


class Tsne:
    def plotIris(self):
        iris = load_iris()
        X_tsne = TSNE(learning_rate=100).fit_transform(iris.data)
        print(pd.DataFrame(X_tsne).head())
        X_pca = PCA().fit_transform(iris.data)
        print(pd.DataFrame(X_pca).head())

        plt.figure(figsize=(10, 5))
        # subplots in 1 row, 2 cols
        plt.subplot(121)
        plt.title("tsne")
        plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=iris.target)
        plt.subplot(122)
        plt.title("pca")
        plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target)
        plt.show()

    # def plotNewsgroups(self):
    #     categories = ['alt.atheism', 'talk.religion.misc', 'comp.graphics', 'sci.space']
    #     ng = fetch_20newsgroups(categories=categories)
    #     X_tsne = TSNE(learning_rate=100, init='pca').fit_transform(ng)
    #
    #     plt.figure(figsize=(10, 5))
    #     plt.title("tsne")
    #     plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=ng.target)
    #     plt.show()

    def plotDigits(self):
        digits = load_digits()
        X = digits.data
        y = digits.target

        def plot_embedding(X, title=None):
            x_min, x_max = np.min(X, 0), np.max(X, 0)
            X = (X - x_min) / (x_max - x_min)

            plt.figure()
            ax = plt.subplot(111)
            for i in range(X.shape[0]):
                plt.text(X[i, 0], X[i, 1], str(digits.target[i]),
                         color=plt.cm.Set1(y[i] / 10.),
                         fontdict={'weight': 'bold', 'size': 9})

            if hasattr(offsetbox, 'AnnotationBbox'):
                # only print thumbnails with matplotlib > 1.0
                shown_images = np.array([[1., 1.]])  # just something big
                for i in range(digits.data.shape[0]):
                    dist = np.sum((X[i] - shown_images) ** 2, 1)
                    if np.min(dist) < 4e-3:
                        # don't show points that are too close
                        continue
                    shown_images = np.r_[shown_images, [X[i]]]
                    imagebox = offsetbox.AnnotationBbox(
                        offsetbox.OffsetImage(digits.images[i], cmap=plt.cm.gray_r),
                        X[i])
                    ax.add_artist(imagebox)
            plt.xticks([]), plt.yticks([])
            if title is not None:
                plt.title(title)

        seed = 5
        tsne = TSNE(n_components=2, init='pca', random_state=seed)
        t0 = time()
        X_tsne = tsne.fit_transform(X)
        plot_embedding(X_tsne, "t-SNE embedding of the digits (time %.2fs)" % (time() - t0))
        plt.show()

        # X_tsne = tsne.fit_transform(X)
        # plt.title('tsne digits')
        # plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y)
        # plt.annotate(y,(X_tsne[:, 0], X_tsne[:, 1]))
        # plt.show()
        # print(time() - t0)

    def plotDigits2(self):
        seed = 42
        tsne = TSNE(random_state=seed)
        digits = load_digits()
        digits_tsne = tsne.fit_transform(digits.data)

        plt.figure(figsize=(10, 10))
        plt.title("digits classificationo using TSNE")
        plt.xlim(digits_tsne[:, 0].min(), digits_tsne[:, 0].max() + 1)
        plt.ylim(digits_tsne[:, 1].min(), digits_tsne[:, 1].max() + 1)
        colors = ["#476A2A","#7851B8","#BD3430","#4A2D4E","#875525","#A83683","#4E655E","#853541","#3A3120","#535D8E"]
        for i in range(len(digits.data)):
            # actually plot the digits as text instead of using scatter
            plt.text(digits_tsne[i, 0], digits_tsne[i, 1], str(digits.target[i]), color=colors[digits.target[i]], fontdict={'weight': 'bold', 'size': 9})
            plt.ylabel("t-SNE feature 0")
            plt.xlabel("t-SNE feature 1")
        plt.show()


if __name__ == "__main__":
    t = Tsne()
    # t.plotIris()
    # t.plotNewsgroups()
    # t.plotDigits()
    t.plotDigits2()
