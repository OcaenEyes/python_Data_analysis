import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


'''
    折线图，用直线段将各数据连接起来组成的图形
    常用来观察数据随时间变化的趋势
    例如：股票价格，温度变化
'''

date ,open ,close = np.loadtxt("000001.csv",delimiter=',',converters={0:mdates.bytespdate2num('%Y-%m-%d')},skiprows=1,usecols=(0,1,3),unpack=True)

plt.plot_date(date,open,linestyle='--',color="green",marker="<")
plt.plot_date(date,open,linestyle='-',color="red",marker ='o')
plt.show()