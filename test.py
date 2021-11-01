from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

xx = np.linspace(0,99000, 100)
rv = stats.norm(40000,20000)
cdf = rv.cdf(xx)
# diff_grade = int(rv.cdf(d)*9999)
plt.plot(xx, cdf)
plt.show()