import numpy as np
import matplotlib.pyplot as plt

x= np.arange(-10,11,1)
y = x*x
plt.plot(x,y)
# 加入注释
plt.annotate("this is the bottom",xy = (0,1),xytext=(0,20),
             arrowprops = dict(facecolor = 'r',headlength=20,headwidth =20,width=30))
plt.show()


