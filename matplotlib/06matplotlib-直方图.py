import numpy as np
import matplotlib.pyplot as plt

'''
    由于一系列不等的纵形图组成，表示数据分布的情况
    例如：某年级同学的身高分布
    需要注意与 柱形图的区别
'''

# # 例
# mu = 100    #均值
# sigma = 20    # 标准差
#
# x = mu + sigma * np.random.random(1000)
# plt.hist(x,bins=20,density=True)
# plt.show()
#
#
# # 双变量图 频率越低越暗
# # x的中心为2
# x = np.random.randn(1000) +2
# # y的中心为3
# y = np.random.randn(1000)+3
#
# plt.hist2d(x,y,bins=40)
# plt.show()


# 练习
'''
    随机生成2000个数据，均值为10， 方差3；
    绘制两个直方图， bins =10 和50 ，normed ／density 分别为True,False;
    随机生成x,y 各2000个， x均值1 ，y 均值5;
    绘制2-D直方图， bins = 40;
'''
# 均值
ava = 10
# 方差
variance = 3

sigma = np.sqrt(variance)
x = ava + sigma * np.random.random(2000)

plt.hist(x,bins=10,density=True)
plt.show()

plt.hist(x,bins=50,density=False)
plt.show()

x = np.random.randn(2000) +1
y = np.random.randn(2000) + 5
plt.hist2d(x,y,bins=40)
plt.show()
