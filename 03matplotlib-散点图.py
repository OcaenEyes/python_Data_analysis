import numpy as np
import matplotlib.pyplot as plt

'''
    散点图显示两组数据的值，每个点的坐标位置的值决定
    用户观察两种变量的相关性：
        正相关
        负相关
        不相关
        
'''

# 正相关
height = [161,170,174,165,182,175]
weight = [50,65,70,62,81,75]
plt.scatter(height,weight)
plt.show()


# 不相关
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
plt.scatter(x,y)
plt.show()


# 散点图的外观
'''
    c    颜色
    s    点（面积）大小
    alpha       透明度
        值的范围[0,1]
        通过调节透明度，来观察点的集中性
    marker      点形状
'''


# 练习
'''
    使用000001.csv的数据
    计算最高价 和开盘价之差
    绘出前后两天diff的散点图， 研究是否具有相关性
    
'''
height,open = np.loadtxt('000001.csv',delimiter=',',skiprows=1,usecols=(2,1),unpack=True)
change = height -open
tomorrow = change[2:]
yesterday = change[:-2]
plt.scatter(yesterday,tomorrow,alpha=0.2,)
plt.show()