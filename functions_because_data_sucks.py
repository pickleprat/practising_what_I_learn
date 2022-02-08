import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np
plt.style.use('ggplot')
x = np.random.randint(1, 1000, (1000, 1))
y = np.random.randint(1, 2000, (1000, 1))
z = np.sin(x)
orange = np.random.randint(0, 301, (250, 1))
orangey = np.random.randint(1000, 2000, (250, 1))

redx = np.random.randint(400, 1001, (100, 1))
redy = np.random.randint(0, redx-400, (100, 1))

plt.plot(x , y, 'ob--',  label='Random values')
plt.plot(x, z, '.g-', label='Random Sine wave')
plt.plot(orange, orangey, 'oc--', label='Painting')
plt.plot(redx, redy, 'or--', label='Weird Ass Triangle')

plt.title('Some mathematical fucntions')

plt.xlabel='Input  ranges'

plt.ylabel='Output values'

plt.grid(True)

plt.savefig('./images_from_matplotlib/rando_ugly_painting')

plt.tight_layout()

plt.show()

