import numpy as np

# ndarray

'''
    # 三种创建方式
    1、从python的基础数据对象转化
    2、通过numpy内置的函数生成
    3、从硬盘（文件）读取数据
'''
# 创建方法一
a= [1,2,3,4]
x1 = np.array(a)
print(x1,"\n",type(x1))

# 创建方法二
x = np.arange(5)
print(x,"\n",type(x))

# # 创建方法三
# date,Open,low = np.loadtxt('..csv',delimiter="\t",skiprows=1,usecols=(1,2,4),unpack=True)
# print(date,"\n",Open,"\n",low)


# 常用函数
'''
    min     最小值
    max     最大值
    median      中值
    mean        均值
    variance        方差
    sort        
'''

c = np.random.randint(1,100,10)
print(np.sort(c))
print(np.mean(c))


# 练习
'''
    使用numpy生成100以内的随机数组
    将数组存储到文件，再从文件中读取数组
    对数据进行sort ,max ,min ,mean ,variance
'''

N1 = np.random.randint(0,100,10)
# 将N1 存储到文件中
np.savetxt("0002.cvs",N1,fmt = "%d",delimiter=",",header="number")
# 从文件中读取数组
N2 = np.loadtxt("0002.cvs",delimiter=",",skiprows=1)

print(np.sort(N2))
print(np.max(N2))


