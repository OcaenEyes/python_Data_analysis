import numpy as np
import matplotlib.pyplot as plt

'''
    颜色：
    - 八种内置默认颜色， 缩写
        b   :blue
        g   :green
        r   :red
        c   :cyan
        m   :magenta
        y   :yellow
        k   :black
        w   :white
    - 其它颜色的表示方法
        灰色阴影
        html   十六进制
        RGB    元组
        
'''

y = np.arange(1,5)
# 内置颜色表示
plt.plot(y,color ='g')
# 灰度表示方法
plt.plot(y+1,color = '0.5')
# html 十六进制
plt.plot(y+2,color = '#ff00ff')
# RGB 元组
plt.plot(y+3,color=(0.1,0.2,0.3))

plt.show()


'''
    线
        linestyle =''
        --      虚线
        -.      点化线
        ：      点线
        -       实线
        
    样式字符串
        可将 颜色，点型，线性 ，依次排列成一个字符串如：
            cx--
            mo:
            kp-
            
            plt.plot(y,'cx--')
'''

# 练习
'''
    使用样式字符串绘制两条线；
        1、红色，实线，圆点
        2、黄色，虚线，X点
        3、绿色，点线，三角形点
'''

y = np.arange(0,4)
plt.plot(y,'ro-',y+1,'yx--',y+2,'g>:')

plt.show()