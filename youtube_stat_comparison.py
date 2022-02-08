from cProfile import label
import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt

plt.style.use('ggplot')

mr_beast = pd.read_csv('./comma_seperated_values/MrBeast_youtube_stats.csv')
cocomelon = pd.read_csv('./comma_seperated_values/cocomelon.csv')
mr_beast=mr_beast.head(10)
cocomelon=cocomelon.head(10)
plt.plot(mr_beast['publishTime'], mr_beast['viewCount'], '.b-', label='MrBeast')

plt.plot(mr_beast['publishTime'], cocomelon['viewCount'], '.y--', label='CocoMelon')

plt.grid(True)
plt.title('Youtube comparison')

plt.legend()

plt.xlabel='Published day'

plt.ylabel='Number of views'

plt.show()
