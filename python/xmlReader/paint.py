import numpy as np
import matplotlib.pyplot as plt
import random

Y = []
X = []
for i in range(0,30):
    X.append(i)
    Y.append(random.uniform(0.85, 0.96))

plt.figure()
plt.plot(range(Y.__len__()),Y)
plt.show()