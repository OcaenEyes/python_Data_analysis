import numpy as np
import matplotlib.pyplot as plt
# 例1
x = np.arange(2,20,1)
y1 = x*x
y2 = np.log(x)
plt.plot(x,y1)
# 添加坐标轴
plt.twinx()
plt.plot(x,y2)
plt.show()

# 例2
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x,y1)
ax1.set_ylabel('Y1')

ax2 = ax1.twinx()
ax2.plot(x,y2,'r')
ax2.set_ylabel('Y2')
ax1.set_xlabel('Compare Y1 and Y2')

plt.show()