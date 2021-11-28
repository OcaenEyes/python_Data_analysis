#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# 交互方式
y = np.arange(1,10,1)
plt.grid(color='r',linewidth= 2,linestyle='--')
plt.plot(y,y*2)
plt.show()

# 面向对象方式
x= np.arange(1,10,1)
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(x,x*2)
ax.grid(color='g',linewidth=2,linestyle='--')
plt.show()

# 练习
'''
    使用plt 和面向对象方式绘制网格
        绿色线
        点划线
        宽度为1
'''
x1 = np.arange(1,10,1)
plt.grid(color='g',linewidth=1,linestyle='-.')
plt.plot(x1,x1 *2)
plt.show()

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
plt.plot(x1, x1 *2)
ax2.grid(color='g',linewidth=1,linestyle='-.')
plt.show()

