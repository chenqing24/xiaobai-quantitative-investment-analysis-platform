'''
 # @ Author: Jeff Chen
 # @ Create Time: 2023-11-09 15:28:12
 # @ Description: 本地数据管理和数据处理
 '''

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import datetime as dt
from matplotlib import dates as mdates
import HP_global as g
from HP_set import *


## 数据处理
#g.path = '当前路径/xbdata'


def stockname(n):
    '''数字股票代码转字符串股票代码

    Parameters:
        n: 
    Returns:
        str:
    '''

    s = str(n).strip()

    if (len(s)<6 and len(s)>0):
        # 字符串长度用0补足6位
        s = s.zfill(6) + '.SZ' # 000开头的是深股
    if len(s)==6:
        if s[0:1]=='0':
            s = s + '.SZ'
        else:
            s = s + '.SH' # 非0开头的默认沪股

    return s


def jqtots(df1):
    '''聚宽格式转ts格式'''
    a = [x.strftime("%Y-%m-%d") for x in df1.index]
    df1.insert(0, 'date', a)

    df1 = df1.reset_index(level=None, drop=True, col_level=0, col_fill='')

    return df1


def tstojq(df1):
    '''ts格式转聚宽格式'''
    a = [dt.datetime.strptime(x, "%Y-%m-%d") for x in df1['date']]

    df1.insert(0, 'date2', a)
    df1 = df1.reset_index(level=None, drop=True, col_level=0, col_fill='')
    df1.index = df1['date2']
    del df1['date2']
    del df1['date']

    return df1


# 测试用例
if __name__ == '__main__':
    print('stockname(000678) = ', stockname(678))
    print('stockname(600026) = ', stockname(600026))

