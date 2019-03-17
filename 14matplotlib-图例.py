#!/usr/bin/python
# -*-coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,11,1)
plt.grid(True)
plt.plot(x,x*2,label = 'Normal')
plt.plot(x,x*3,label='Fast')
plt.plot(x,x*4,label='Faster')

#开启图例
plt.legend(loc=1,ncol=2)
# plt.legend(['Normal','Fast','Faster'],loc=1,ncol=2)
# 常用的图例参数
# loc = [0-10]  : 调整图例的位置
# ncol          ：调整图例有几列
plt.show()

# 面向对象的方法
fig = plt.figure()
ax = fig.add_subplot(111)

l, = plt.plot(x,x)
plt.legend(['ax legend'])

# l.set_label('label via method')
# #显示图例
# ax.legend()

# l, = plt.plot(x,x,label = 'Inline label')
# ax.legend()

plt.show()