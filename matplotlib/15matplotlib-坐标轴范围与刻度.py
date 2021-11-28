#!/usr/bin/python
# -*-coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# 坐标轴范围
# 根据需求调整坐标轴范围

x = np.arange(-10,11,1)
plt.plot(x,x*x)
# 调整坐标轴范围
# 只调x轴，  xmin ,xmax
plt.xlim([-8,8])
# 只调y轴，  ymin .ymax
plt.ylim(0,60)
# 同时调整 x轴[-10,4] ， y轴[20,80]
plt.axis([-10,4,20,80])
plt.show()


# 坐标轴刻度
# 1 调整数字刻度
x = np.arange(1,11,1)
y = x+1

ax = plt.plot(x,y)
# 获取当前图形的坐标轴
ax = plt.gca()
# 指定x,y轴刻度为10
ax.locator_params(nbins =10)
# #指定x轴
# ax.locator_params('x',nbins =20)
# #指定y轴
# ax.locator_params('y',nbins = 20)
plt.grid()
plt.show()


# 2 调整日期刻度
import datetime
import matplotlib as mpl

fig = plt.figure()
start = datetime.datetime(2015,1,1)
stop = datetime.datetime(2016,1,1)
delta = datetime.timedelta(days=1)

dates = mpl.dates.drange(start,stop,delta)

y = np.random.rand(len(dates))

ax = plt.gca()
ax.plot_date(dates,y,linestyle='-',marker='')

# 设置日期格式
date_format = mpl.dates.DateFormatter('%Y-%m')
ax.xaxis.set_major_formatter(date_format)

# 自适应图
fig.autofmt_xdate()

plt.show()
