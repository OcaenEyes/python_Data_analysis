import numpy as np
import matplotlib.pyplot as plt

# 柱形图
# 例一
N =5
y =  [15,28,10,30,25]
index = np.arange(N)
p = plt.bar(index,height=y)
plt.show()

# 例2
p1 = plt.bar(0,bottom=index,width=y,height=0.5,align='edge',color='red',orientation='horizontal')
plt.show()

p2 = plt.barh(index,width= y , align='edge',color ='green',height=0.5)
plt.show()

# 例3
sales_BJ = [52,55,63,53]
sales_SH = [44,66,55,41]

index = np.arange(4)
bar_width = 0.3

# 竖着显示
plt.bar(index,sales_BJ,bar_width)
plt.bar(index+bar_width,sales_SH,bar_width,color='r')
plt.show()

# 横着显示
plt.barh(index,sales_BJ,bar_width)
plt.barh(index+bar_width,sales_SH,bar_width,color='r')
plt.show()

# 层叠图
plt.bar(index,sales_BJ,bar_width)
plt.bar(index,sales_SH,bar_width,color='r',bottom=sales_BJ)
plt.show()

# 练习
'''
    生成两组大小为5的数据；
    画出两组数据 水平的条形图；
    采用并列，层叠两种方式；
    
'''

N =5
n1 = np.random.randint(1,100,N)
n2 = np.random.randint(1,100,N)

index = np.arange(N)
bar_width = 0.3

# 并列显示
plt.bar(index,n1,bar_width)
plt.bar(index+bar_width,n2,bar_width,color='r')
plt.show()

# 层叠显示
plt.bar(index,n1,bar_width)
plt.bar(index,n2,bar_width,color='r',bottom=n1)
plt.show()
