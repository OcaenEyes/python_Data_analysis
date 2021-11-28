#!/usr/bin/python
# -*- coding:utf-8 -*-


# 环境准备
try:
    import os
    import tushare as ts
    import pandas as pd
    import matplotlib.pyplot as plt
except:
    os.system('pip install tushare')
    os.system('pip install pandas')
    os.system('pip install matplotlib')

# 获取中国平安三年内K线数据
ZGPA = ts.get_hist_data('000001')
# ZGPA.to_csv('000001.csv')
ZGPA.index = pd.to_datetime(ZGPA.index)


# 相关指数
print(ZGPA.tail())
plt.plot(ZGPA['close'],label='收盘价')
plt.plot(ZGPA['ma5'],label='MA5')
plt.plot(ZGPA['ma20'],label='MA20')
plt.legend()

plt.xlabel('日期')
plt.ylabel('股价')
plt.title('中国平安收盘价，MA5，MA20时间序列')
plt.show()



# 获取中国平安全部历史数据
ZGPA_all = ts.get_h_data('000001',start='2016-01-01')
ZGPA_all.index = pd.to_datetime(ZGPA_all.index)

# 相关指数
print(ZGPA_all.tail())
plt.plot(ZGPA_all['close'],label = '收盘价')
plt.legend()
plt.xlabel('日期')
plt.ylabel('股价')
plt.title('中国平安收盘价时间序列（2016至今）')

plt.show()

# 计算收益率
ZGPA_return = ((ZGPA_all['close'] - ZGPA_all['close'].shift(1)) / ZGPA_all['close'].shift(1)).dropna()
plt.plot(ZGPA_return)
plt.show()

print('中国平安的平均日收益率：',ZGPA_return.mean())
print('中国平安的收益率标准差：',ZGPA_return.std())
