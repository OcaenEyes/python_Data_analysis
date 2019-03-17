import numpy as np
import matplotlib.pyplot as plt

'''
    箱形图（Box-plot）又称为盒须图，盒式图，或 箱线图；
    是一种用在显示一组数据分散情况的资料统计图；
    上边缘，上四分位数，中位数，下四分位数，下边缘，异常值；
'''

np.random.seed(100)
data = np.random.normal(size=1000,loc=0,scale=1)
# sym 指定异常值的点；whis虚线的长度， 通过调整whis的大小来决定收入异常值的多少
plt.boxplot(data,sym ='o',whis=1.5)
plt.show()

# 同一张图中显示多个箱线图

# 4组 1000的数据
data = np.random.normal(size=(1000,4),loc = 0,scale=1)
# 每组的标签为ABCD
labels = ['A','B','C','D']

plt.boxplot(data,labels=labels)
plt.show()


# 练习
'''
    随机生成 100 *5 的数组；
    绘制箱线图，使用sym ,whis参数
    
'''
data = np.random.normal(size=(100,5),loc = 0,scale=1)
plt.boxplot(data,sym='o',whis=0.5)
plt.show()