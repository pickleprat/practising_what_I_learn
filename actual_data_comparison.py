import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt
plt.style.use('ggplot')

dta = pd.read_csv('./comma_seperated_values/health_injuries.csv')
dta=dta.head(10)

plt.plot(dta['Period'], dta['Data_value'], 'ob-', label='Real data values')

plt.plot(dta['Period'], dta['Lower_CI'], '.k--', label='Lower Probabilities')

plt.plot(dta['Period'], dta['Upper_CI'], 'og-', label='Upper Probabilities')

plt.grid(True)

plt.xlabel='Year interval'

plt.ylabel='Number of injuries'

plt.title='Health Injury Analysis'

plt.legend()

plt.show()

