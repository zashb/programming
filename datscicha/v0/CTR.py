import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2


class DataGen:
    def __init__(self, p1, p2):
        # p1,p2 => prob of click for adv1,adv2
        self.p1 = p1
        self.p2 = p2

    # ret res whether a person clicked on adv1 or adv2
    def next(self):
        click1 = 1 if np.random.random() < self.p1 else 0
        click2 = 1 if np.random.random() < self.p2 else 0
        return click1, click2


def getP(contingTab):
    det = contingTab[0, 0] * contingTab[1, 1] - contingTab[0, 1] * contingTab[1, 0]
    testStat = float(det) / contingTab[0].sum() * det / contingTab[1].sum() * \
               contingTab.sum() / contingTab[:, 0].sum() / contingTab[:, 1].sum()
    pVal = 1 - chi2.cdf(x=testStat, df=1)
    return pVal


def runExp(p1, p2, N):
    data = DataGen(p1, p2)
    p_values = np.empty(N)
    continTab = np.zeros((2, 2)).astype(np.float32)
    for i in range(N):
        c1, c2 = data.next()
        continTab[0, c1] += 1
        continTab[1, c2] += 1
        # because we are dividing by rowsum and colsum
        if i < 10:
            p_values[i] = None
        else:
            p_values[i] = getP(continTab)
    plt.plot(p_values)
    plt.plot(np.ones(N) * 0.05)
    plt.show()


if __name__ == "__main__":
    runExp(0.1, 0.11, 20000)

    # p-val in the graph should be below the threshold 5% of the time
