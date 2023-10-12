#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:33:31 2023
模仿通达信公式指标 KDJ
@author: qingchen
"""
import os
import numpy as np
import pandas as pd
import tushare as ts
from dotenv import load_dotenv


# 平均函数
def MA(Series, N):
    return pd.Series.rolling(Series, N).mean()

def SMA(Series, N, M=1):
    ret =[]
    i = 1
    length = len(Series)
    
    # 跳过X中前面的几个nan值
    while i<length:
        if np.isnan(Series.iloc[i]):
            i += 1
        else:
            break
    
    preY = Series.iloc[i]   # Y轴
    ret.append(preY)
    
    while i<length:
        Y = (M * Series.iloc[i] + (N - M) * preY) / float(N)
        ret.append(Y)
        preY = Y
        i += 1
        
    return pd.Series(ret, index=Series.tail(len(ret)).index)

def HHV(Series, N):
    return pd.Series(Series).rolling(N).max()

def LLV(Series, N):
    return pd.Series(Series).rolling(N).min()


# 获取股票 新希望 的k日线数据，已经是老版本不可用
# 新版：从配置中读取token，在通过sdk获取数据
load_dotenv()
token = os.getenv("TUSHARE_TOKEN")
ts.set_token(token)
pro = ts.pro_api()

# 获取交易日历信息
# df = pro.trade_cal(exchange='', start_date='20230901', end_date='20231001', 
#                    fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
data = pro.daily(ts_code="000876.SZ", start_date=20230101)
print(data)

# 初始化
# data = ts.get_k_data('000876', ktype='D')
mydf = data.copy()  # 建立新的股票数据序列，防止原数据损坏

CLOSE   = mydf['close'] # 收盘价
LOW     = mydf['low']   # 最低价
HIGH    = mydf['high']  # 最高价
OPEN    = mydf['open']  # 开盘价
VOL     = mydf['vol']   # 成交量
# 简称
C   = mydf['close']
L   = mydf['low']
H   = mydf['high']
O   = mydf['open']
V   = mydf['vol']


def KDJ(N=9, M1=3, M2=3):
    
    RSV = (CLOSE - LLV(LOW, N)) / (HHV(HIGH, N) - LLV(LOW, N)) * 100
    K = SMA(RSV, M1, 1)
    D = SMA(K, M2, 1)
    J = 3 * K - 2 * D
    
    return K, D, J


# 计算后的指标加入股票数据序列中
K, D, J = KDJ()
mydf = mydf.join(pd.Series(K, name='K'))
mydf = mydf.join(pd.Series(D, name='D'))
mydf = mydf.join(pd.Series(J, name='J'))

# 增加上轨迹80线，下轨迹20线
mydf['S80'] = 80
mydf['X20'] = 20

# 显示最后100条数据
mydf = mydf.tail(100)


# 绘制图形
mydf.S80.plot.line()
mydf.X20.plot.line()
mydf.K.plot.line(legend=True)
mydf.D.plot.line(legend=True)
mydf.J.plot.line(legend=True)

print("done")