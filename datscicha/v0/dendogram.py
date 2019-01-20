import plotly.figure_factory as ff
from plotly.offline import plot

import numpy as np

X = np.random.rand(15, 15)
print(X)
dendro = ff.create_dendrogram(X)
dendro['layout'].update({'width': 800, 'height': 500})
plot(dendro,
     filename=r'C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\plots\simple_dend.html')
