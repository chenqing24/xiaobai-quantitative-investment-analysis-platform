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
