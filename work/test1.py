import numpy as np
import pandas as pand
import matplotlib.pyplot as plt
from pylab import *

x = np.random.randn(1000)
plt.hist(x,100)
savefig('test.png',format='png')