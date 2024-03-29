#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

'''
    - matplotlib 对象简介
        FigureCanvas
        Figure
        Axes
    - figure = plt.figure()
        Figure 实例
        可以添加axes实例
    
    - ax =fig.add_subplot(111)
        返回Axes实例；
        参数一： 子图总行数
        参数二： 子图总列数
        参数三： 子图位置
        在Figure上添加Axes的常用方法
        
'''

# 生成一个序列
x = np.arange(1,100)

# 生成一个对象
fig = plt.figure()

# 生成一个 2*2 的子图结构
ax1 = fig.add_subplot(221)
ax1.plot(x,-x)

ax2 = fig.add_subplot(222)
ax2.plot(x,x)

ax3 = fig.add_subplot(223)
ax3.plot(x,x*x)

ax4 = fig.add_subplot(224)
ax4.plot(x,np.log(x))

plt.show()