# coding:utf-8


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

y = [0.524251806,0.440660475,0.406088751,0.40505676,0.441692466,0.492260062,0.45252838,0.465944272,0.541795666,0.663054696,1]
x = [350,250,150,110,80,50,35,25,15,7,4]


cof = np.polyfit(x,y,10)           # 调用函数，用 3 次多项式拟合
print(cof)                              # 返回多项式的系数

p=np.poly1d(cof)

plt.plot(x,y,'o',x,p(x),lw=2)
plt.show()