#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

'''
    三种方式简介
        - pyplot : 经典高层封闭
        - pylab : 将matplotlib  和 numpy 合并的模块， 模拟matlab的编程环境
        - 面向对象的方式，matplotlib的精髓， 更基础和底层的方式
    
    三种方式优劣
        - pyplot : 简单易用，交互使用时方便，可以根据命令实时作图； 但 底层定制能力不足
        - pylab : 完全封装，环境最接近matlab 
        - 面向对象（Object-Oriented）的方式：接近matplotlib基础和底层的方式， 难度稍大
        
    实战中推荐，综合使用pyplot 和 OO的方式， 显示导入numpy
'''

# 例
x = np.arange(0,10,1)
y = np.random.rand(len(x))

fig = plt.figure()
ax = fig.add_subplot(111)

l, = plt.plot(x,y)
t = ax.set_title('obj')

plt.show()