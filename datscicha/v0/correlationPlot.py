import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# import seaborn as sns


class correlationPlot:
    def matplotlibPlot(self):
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
        names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
        data = pd.read_csv(url, names=names)
        correlations = data.corr()
        print(correlations[:10])
        # plot correlation matrix
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(correlations, vmin=-1, vmax=1)
        fig.colorbar(cax)
        ticks = np.arange(0, 9, 1)
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.set_xticklabels(names)
        ax.set_yticklabels(names)
        plt.show()

        # def seabornPlot(self):
        #     url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
        #     names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
        #     data = pd.read_csv(url, names=names)
        #     correlations = data.corr()
        #     print(correlations[:10])
        #     sns.heatmap(correlations,vmin=-1,vmax=1)
        #     sns.plt.show()


if __name__ == "__main__":
    cp = correlationPlot()
    cp.matplotlibPlot()
    # cp.seabornPlot()
