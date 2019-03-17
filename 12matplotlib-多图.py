#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 通过创建多个figure 对象来创建多图
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot([1,2,3],[3,2,1])

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot([1,2,3],[2,3,4])

plt.show()
