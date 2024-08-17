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
from HP_download import *


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


def get_k_data(stock_code, start_date=None, end_date=None, ktype='D'):
    '''获取股票K线数据

    Parameters:
        stockcode: 股票代码
        startdate: 开始日期
        enddate: 结束日期
    Returns:
        DataFrame:
    '''
    stockcode = stockname(stockcode)

    data_file_name = ''
    if ktype == 'D':
        # 日线
        data_file_name = os.path.join(g.datapath, stockcode + '_daily.csv')
    else:
        # 错误：未知格式
        raise TypeError('未知ktype: {}'.format(ktype)+ ' 目前仅支持日线数据')

    if data_file_name.endswith('.csv'):
        # 如果文件不存在，尝试先下载
        if not os.path.exists(data_file_name):
            download2csv(code_name=stockcode)

        df = pd.read_csv(data_file_name, index_col=0, parse_dates=True)
        if g.isDbug:
            print(df)
    else:
        # 错误：未知数据文件后缀
        raise TypeError('未知数据文件后缀: {}'.format(data_file_name))
    
    return df


# 测试用例
if __name__ == '__main__':
    print('stockname(000678) = ', stockname(678))
    print('stockname(600026) = ', stockname(600026))

