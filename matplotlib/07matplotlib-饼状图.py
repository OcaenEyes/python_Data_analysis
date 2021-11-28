import numpy as np
import matplotlib.pyplot as plt

'''
    饼状图显示一个数据系列中各项总和的比例；
    饼状图中的数据点显示为整个饼状图的百分比；
    如：前十大品牌占市场份额图
    
'''
# 例
labels = 'A','B','C','D'
fracs = [15.0,30.0,45.0,10.0]

explode = [0,0.05,0,0.08]
plt.axes(aspect=1)
plt.pie(x=fracs,labels=labels,autopct="%.0f%%",explode=explode,shadow=True)
plt.show()

# 练习
labels = 'SH','BJ','SZ','GZ'
fracs = [20,30,25,15]
explode = [0,0,0.08,0]
plt.pie(x= fracs,labels=labels,autopct='%.00f%%',explode=explode,shadow=True)
plt.show()
